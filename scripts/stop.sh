#!/bin/bash

# Stop django server
echo "Stopping project server..."
if ! kill $(pgrep -f "python manage.py runserver"); then
    echo "Failed to stop the project server."
    echo "Please ensure the project is running before running the stop script."
    exit 1
fi

# Inform user the server is stopped
echo "Project server stopped."
