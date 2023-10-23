#!/bin/bash

# Initialize a variable to count failures
failures=0

# Function to run a command and check for errors
run_command() {
  "$@"
  local status=$?
  if [ $status -ne 0 ]; then
    echo "Error: $1 command failed with status $status."
    failures=failures+1
    exit "total failures: $failures"
  fi
}

# Stop React front-end (if running)
pm2 stop front-End

# Stop the Flask back-end(if running)

# Stop and remove Docker database container
docker stop postgres
docker rm postgres

# Remove installed software and dependencies
run_command sudo apt remove -y docker.io docker-compose
run_command sudo apt remove -y python3
run_command sudo apt remove -y python3-pip
run_command sudo apt remove -y nodejs npm

# Clean up any additional files or configurations
rm Back-End/Logs/*
cd Back-End/Database
sed -i 's/user="$postgres_user",/user=os.environ.get("USER"),/' config.py
sed -i 's/password="$postgres_password",/password=os.environ.get("PASSWORD"),/' config.py

# Check the number of failures and prompt the user
if [ $failures -gt 0 ]; then
    echo "Uninstallation encountered $failures failures."
    read -p "Do you want to try uninstalling again (y) or quit (q)? " choice
    if [ "$choice" == "y" ]; then
        ./uninstall.sh
    else
        echo "Existing uninstallation."
    fi
else
    echo "Uninstallation successful."
fi
