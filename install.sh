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

# Prompt for PostgreSQL environment variables
read -p "Enter your PostgreSQL username: " postgres_user
read -s -p "Enter your PostgreSQL password: " postgres_password

# Update and upgrade the system
run_command sudo apt update
run_command sudo apt upgrade -y

# Install required software
run_command sudo apt install -y docker.io docker-compose
run_command sudo apt install -y python3
run_command sudo apt install -y python3-pip
run_command sudo apt install -y nodejs
run_command sudo apt install -y npm

# Start Docker and enable it to start on boot
run_command sudo systemctl start docker
run_command sudo systemctl enable docker

# Install PostgreSQL Docker container with user-provided credentials
run_command docker run --name postgres -e POSTGRES_USER="$postgres_user" -e POSTGRES_PASSWORD="$postgres_password" -d -p 5432:5432 postgres:latest

# Install back-end dependencies
cd BankingApp/Back-End
run_command pip3 install -r requirements.txt

# Configure database config file and setup database
cd Database
sed -i "s/user=os.environ.get(\"USER\"),/user=\"$postgres_user\",/" config.py
sed -i "s/password=os.environ.get(\"PASSWORD\"),/password=\"$postgres_password\",/" config.py
run_command python3 DatabaseSetup.py

# Run unit tests
cd Tests/UnitTests/DALTests
run_command python3 -m pytest SessionDALTests.py
run_command python3 -m pytest CustomerDALTests.py
run_command python3 -m pytest BankAccountDALTests.py
cd ../../../Database
run_command python3 ResetDatabaseTest.py
cd ../Tests/UnitTests/SALTests
run_command python3 -m pytest SessionSALTests.py
run_command python3 -m pytest CustomerSALTests.py
run_command python3 -m pytest BankAccountSALTests.py
cd ../../../Database
run_command python3 ResetDatabaseTest.py

# Start the back-end server for end-to-end tests
cd ..
nohup python3 run.py &

# Install Node.js dependencies and start the react front-end for end-to-end tests
cd ../../front-end
run_command npm install
pm2 start npm --name "front-end" --start

# Run end-to-end tests
cd ../Back-End/Tests
run_command behave Features

# Reset database for production
cd ../Database
run_command python3 ResetDatabaseProduction.py

# Tell user if install is successful or unsuccessful (if statements will probably need to be included)
if [ $failures -gt 0 ]; then
  echo "Installation encountered $failures failures."
  read -p "Do you want to try again (t) or uninstall (u)? " choice
  if [ "$choice" == "t" ]; then
    echo "Uninstalling..."
    ./uninstall.sh
    ./install.sh
  elif [ "$choice" == "u" ]; then
    echo "Uninstalling..."
    ./uninstall.sh
  else
    echo "Invalid choice. Exiting."
  fi
else
  echo "Installation was successful."
fi
