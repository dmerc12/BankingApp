#!/bin/bash

# Check if project server is already running
echo "Checking if project server is already running..."
if pgrep -f "python manage.py runserver" >/dev/null; then
    echo "The project server is already running."
    echo "If you need to stop the server, please use the stop script."
    exit 1
fi

# Start project server
echo "Starting project server..."
if ! python manage.py runserver; then
    echo "Failed to start the project server."
    exit 1
fi

# Inform user the project server is started
echo "Project server started."
echo "To stop the project server, use the stop script."
