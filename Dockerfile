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

# Copy and run the start script
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh
CMD ["/app/entrypoint.sh"]

#Agregando datos
