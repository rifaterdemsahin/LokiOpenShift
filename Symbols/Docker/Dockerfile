# Use an appropriate base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install bash
RUN apt-get update && apt-get install -y bash

# Install Elasticsearch
RUN apt-get update && apt-get install -y wget gnupg && \
    wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | apt-key add - && \
    sh -c 'echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" > /etc/apt/sources.list.d/elastic-7.x.list' && \
    apt-get update && apt-get install -y elasticsearch

# Install Loki
RUN wget -qO - https://repos.loki.dev/GPG-KEY-loki | tee /etc/apt/trusted.gpg.d/loki.gpg > /dev/null && \
    echo "deb https://repos.loki.dev/deb stable main" > /etc/apt/sources.list.d/loki.list && \
    apt-get update && apt-get install -y loki

# Install htop
RUN apt-get update && apt-get install -y htop
# Update the package list and install procps (which includes top)
RUN apt-get update && apt-get install -y procps
# Copy the application code
COPY . /app

# Install required packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose necessary ports
EXPOSE 9200 3100

# Set the default command for the container
CMD ["python", "main.py"]