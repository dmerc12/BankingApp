#!/bin/bash

# Prompt user for database info
read -p "Enter database host: " db_host
read -p "Enter database name: " db_name
read -p "Enter database port: " db_port
read -p "Enter database username: " db_user
read -s -p "Enter database password: " db_password
echo ""

# Prompt user for inial admin info
read -p "Enter admin username: " admin_username
read -p "Enter admin email: " admin_email
read -s -p "Enter admin password: " admin_password
echo ""
read -s -p "Confirm admin password: " confirm_admin_password
echo ""

# Install dependencies
echo "Installing dependencies..."
if ! pip install django django-jazzmin django-bootstrap5 pandas plotly behave selenium; then
    echo "Failed to install dependencies. Aborting."
    exit 1
fi
echo "Dependencies installed successfully."

# Change into main project directory
cd ../main/ || { echo "Failed to change into main project directory. Aborting."; exit 1; }

# Connect to database
echo "Updating database configuration..."
export DB_HOST=$db_host
export DB_NAME=$db_name
export DB_USER=$db_user
export DB_PORT=$db_port
export DB_PASSWORD=$db_password
echo "Database configuration updated."

# Check database connection
echo "Checking database connection..."
if ! python3 manage.py check; then
    echo "Failed to connect to the database. Aborting."
    exit 1
fi
echo "Database connection successful."

# Run unit tests
echo "Running unit tests..."
if ! python3 manage.py test; then
    echo "Unit tests failed. Aborting."
    exit 1
fi
echo "Unit tests passed."

# Run selenium tests
echo "Running selenium tests..."
cd ../tests/ || { echo "Failed to change into tests directory. Aborting."; exit 1; }
if ! behave features; then
    echo "Selenium tests failed. Aborting."
    exit 1
fi
echo "Selenium tests passed."

# Create initial admin
echo "Creating initial admin..."
if ! python3 manage.py createsuperuser --noinput --username "$admin_username" --email "$admin_email"; then
    echo "Failed to create initial admin. Aborting."
    exit 1
fi
echo "Admin created successfully."

# Inform user install is complete
echo "Installation complete."
echo "Use the run script to run the project."
echo "Use the stop script to stop the running project."
echo "Use the uninstall script to uninstall the project."
