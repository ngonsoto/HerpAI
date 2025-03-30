# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

## Copy application code
COPY . .

# Install make
RUN apt-get update && apt-get install -y make && rm -rf /var/lib/apt/lists/*

# Install dependencies
RUN pip install --no-cache-dir -e .

# Expose ports
EXPOSE 5000 8080

# Run the make script and deploy a webserver to view output files
CMD ["sh", "-c", "make run & python -m http.server -d /app/output 8080"]
