# Use an appropriate base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy the application code
COPY . /app

# Install required packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose necessary ports
EXPOSE 9200 3100

# Set the default command for the container
CMD ["python", "main.py"]