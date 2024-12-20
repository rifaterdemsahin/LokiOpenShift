# Objective: Log OpenShift Events to Elasticsearch/LokiStack for Searchability

## Key Results

### Docker Implementation

#### Step 1: Create Dockerfile
Create a `Dockerfile` to build an image for logging OpenShift events to Elasticsearch/LokiStack.

```Dockerfile
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

# Set the entry point for the container
ENTRYPOINT ["python", "main.py"]
```

#### Step 2: Build Docker Image
Build the Docker image using the Dockerfile.

```sh
docker build -t openshift-logging:latest .
```

#### Step 3: Run Docker Container
Run the Docker container with the necessary environment variables and port mappings.

```sh
docker run -d \
    -e ELASTICSEARCH_HOST=elasticsearch.example.com \
    -e LOKISTACK_HOST=lokistack.example.com \
    -p 9200:9200 \
    -p 3100:3100 \
    openshift-logging:latest
```

#### Step 4: Verify Integration
Verify that the Docker container is running and forwarding OpenShift events to Elasticsearch/LokiStack.

```sh
docker logs <container_id>
```

#### Step 5: Monitor and Maintain
Set up monitoring and alerting for the Docker container to ensure continuous operation and performance.

```sh
docker stats <container_id>
```

#### Sample `main.py` File
Create a `main.py` file to handle logging of OpenShift events to Elasticsearch/LokiStack.

```python
import os
import requests
import json

# Environment variables
ELASTICSEARCH_HOST = os.getenv('ELASTICSEARCH_HOST')
LOKISTACK_HOST = os.getenv('LOKISTACK_HOST')

def log_to_elasticsearch(event):
    url = f"http://{ELASTICSEARCH_HOST}/events"
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data=json.dumps(event))
    return response.status_code

def log_to_lokistack(event):
    url = f"http://{LOKISTACK_HOST}/loki/api/v1/push"
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data=json.dumps(event))
    return response.status_code

def main():
    # Sample event data
    event = {
        "event_type": "OpenShift Event",
        "message": "This is a sample event log",
        "timestamp": "2023-01-01T00:00:00Z"
    }

    # Log event to Elasticsearch
    es_status = log_to_elasticsearch(event)
    print(f"Logged to Elasticsearch: {es_status}")

    # Log event to LokiStack
    loki_status = log_to_lokistack(event)
    print(f"Logged to LokiStack: {loki_status}")

if __name__ == "__main__":
    main()
```