#!/bin/bash

echo "Starting GREEN version..."
uvicorn app.app_green:app --port 8001 &

sleep 5  # wait for startup

echo "Switching traffic to GREEN"
echo "green" > live_version.txt

echo "Stopping BLUE version"
pkill -f "app_blue"
