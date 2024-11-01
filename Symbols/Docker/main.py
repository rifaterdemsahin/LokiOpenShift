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