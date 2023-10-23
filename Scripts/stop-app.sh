#!/bin/bash

# Stop the React front-end
pm2 delete front-end

# Stop the Flask back-end API
pkill -f "python3 run.py"

# Stop the PostgreSQL database
docker stop postgres
