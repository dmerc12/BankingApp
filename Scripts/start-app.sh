#!/bin/bash

# Start the PostgreSQL database
docker start postgres

# Start the Flask back-end API
cd ../Back-End
nohup python3 run.py &

# Start the React front-end
cd ../front-end
pm2 start npm --name "front-end" --start
