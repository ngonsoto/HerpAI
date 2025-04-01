#!/bin/sh

# Create .env file dynamically
echo "SONNET_API_KEY=${SONNET_API_KEY}" > /app/.env
echo "OPENAI_API_KEY=${OPENAI_API_KEY}" >> /app/.env

# Run the application
make run

# Deploy a webserver to show the output
python -m http.server -d /app/output 8080
