# Use official Python runtime as a parent image
FROM python:3.11-slim

# Set working directory in container
WORKDIR /app

# Install netcat for entrypoint DB wait check
RUN apt-get update && apt-get install -y --no-install-recommends netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire project
COPY . .

# Make entrypoint script executable
RUN chmod +x entrypoint.sh

# Expose port 8000 (Django default)
EXPOSE 8000

# Run entrypoint (waits for DB, runs migrations, starts server)
ENTRYPOINT ["./entrypoint.sh"]
