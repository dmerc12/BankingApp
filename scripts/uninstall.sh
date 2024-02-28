#!/bin/bash

# Function to stop project server if it's currently running
stop_server() {
    echo "Checking if project server is already running..."
    if pgrep -f "python manage.py runserver" >/dev/null; then
        echo "Stopping project server..."
        if ! kill $(pgrep -f "python manage.py runserver"); then
            echo "Failed to stop the project server. Aborting."
            exit 1
        fi
            echo "Project server stopped."
    fi
}

# Function to remove database info
remove_database() {
    echo "Removing database information..."
    python manage.py flush
    echo "Database information removed."
}

# Function to remove project files
remove_project_filed() {
    echo "Removing project files..."
    rm -rf ../BankingApp/
    echo "Project files removed."
}

# Main funciton for uninstallation
uninstall() {
    echo "Beginning uninstallation process..."
    stop_server
    remove_database
    remove_project_files
    echo "Uninstallation complete."
}

# Execute uninstall
uninstall
