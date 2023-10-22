#!/bin/bash

# Prompt for PostgreSQL environment variables
read -p "Enter your PostgreSQL username: " postgres_user
read -s -p "Enter your PostgreSQL password: " postgres_password

# Update and upgrade the system
sudo apt update
sudo apt upgrade -y

# Install required software
sudo apt install -y docker.io docker-compose
sudo apt install -y python3
sudo apt install -y python3-pip
sudo apt install -y nodejs
sudo apt install -y npm

# Start Docker and enable it to start on boot
sudo systemctl start docker
sudo systemctl enable docker

# Install PostgreSQL Docker container with user-provided credentials
docker run --name postgres -e POSTGRES_USER="$postgres_user" -e POSTGRES_PASSWORD="$postgres_password" -d -p 5432:5432 postgres:latest

# Install back-end dependencies
cd BankingApp/Back-End
pip3 install -r requirements.txt

# Configure database config file and setup database
cd Database
sed -i "s/user=os.environ.get(\"USER\"),/user=\"$postgres_user\",/" config.py
sed -i "s/password=os.environ.get(\"PASSWORD\"),/password=\"$postgres_password\",/" config.py
python3 DatabaseSetup.py


# Run unit tests, then start back-end server for end-to-end tests
cd Tests/UnitTests/DALTests/
python3 -m pytest SessionDALTests.py
python3 -m pytest CustomerDALTests.py
python3 -m pytest BankAccountDALTests.py
cd ../../../Database
python3 ResetDatabaseTest.py
cd ../Tests/UnitTests/SALTests
python3 -m pytest SessionSALTests.py
python3 -m pytest CustomerSALTests.py
python3 -m pytest BankAccountSALTests.py
cd ../../../Database
python3 ResetDatabaseTest.py
cd ..
nohup python3 run.py &

# Install Node.js dependencies and start the react front-end for end-to-end tests
cd ../../front-end
npm install
pm2 start npm --name "front-end" --start

# Run end-to-end tests
cd ../Back-End/Tests
behave Features

# Reset database for production
cd ..//Database
python3 ResetDatabaseProduction.py

# Tell user if install is successful or unsuccessful (if statements will probably need to be included)

