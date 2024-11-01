#!/bin/bash

# Start Elasticsearch
service elasticsearch start

# Wait for Elasticsearch to be ready (adjust time as necessary)
sleep 10

# Run your Python application
exec python main.py