import logging
import json
import os
from datetime import datetime
from random import choice
import requests

print("Starting log ingestor script...")

# Configuration for logging
LOG_CONFIG = {
    'log1.log': 'info',
    'log2.log': 'error',
    'log3.log': 'debug',
    'log4.log': 'info',
    'log5.log': 'error',
    'log6.log': 'debug',
    'log7.log': 'info',
    'log8.log': 'error',
    'log9.log': 'debug',
}

# Log levels
LOG_LEVELS = {
    'info': logging.INFO,
    'error': logging.ERROR,
    'debug': logging.DEBUG,
    'success': logging.INFO  # Custom level mapped to INFO
}

# Create and configure loggers
loggers = {}

for log_file, log_level in LOG_CONFIG.items():
    logger = logging.getLogger(log_file)
    logger.setLevel(LOG_LEVELS[log_level])

    # Ensure the log file exists
    if not os.path.exists(log_file):
        with open(log_file, 'w') as f:
            pass

    handler = logging.FileHandler(log_file)
    formatter = logging.Formatter('%(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    loggers[log_file] = logger
    print(f"Logger configured for {log_file}")

# Ensure loggers for all API endpoints
api_endpoints = ["posts", "comments", "albums", "photos", "todos", "users"]
for api_name in api_endpoints:
    log_file = f"{api_name}.log"
    if log_file not in loggers:
        logger = logging.getLogger(log_file)
        logger.setLevel(logging.INFO)  # Default level
        handler = logging.FileHandler(log_file)
        formatter = logging.Formatter('%(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        loggers[log_file] = logger
        print(f"Logger configured for {log_file}")

def generate_log(log_file, level, log_string):
    log_entry = {
        "level": level,
        "log_string": log_string,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "metadata": {
            "source": log_file
        }
    }
    return json.dumps(log_entry)

def log_message(api_name, level, log_string):
    log_file = f"{api_name}.log"
    if log_file in loggers:
        log_entry = generate_log(log_file, level, log_string)
        loggers[log_file].log(LOG_LEVELS[level], log_entry)
        print(f"Logged message to {log_file}")
    else:
        print(f"Logger for {log_file} not found.")

# Mock API calls
def mock_api_call(api_name):
    levels = ["info", "error", "success"]
    log_string = f"Log from {api_name}"
    level = choice(levels)

    # Simulate an API call to a mock service
    try:
        response = requests.get(f'https://jsonplaceholder.typicode.com/{api_name}')
        if response.status_code == 200:
            log_message(api_name, level, log_string)
            print(f"API call to {api_name} successful")
        else:
            log_message(api_name, 'error', f"Failed API call to {api_name}")
            print(f"API call to {api_name} failed with status code {response.status_code}")
    except requests.RequestException as e:
        log_message(api_name, 'error', f"Failed API call to {api_name}: {e}")
        print(f"API call to {api_name} failed with exception: {e}")

# Simulate API calls
for _ in range(10):  # Simulate 10 log entries
    api_name = choice(api_endpoints)
    mock_api_call(api_name)
    print(f"Mock API call to {api_name} done")

print("Log ingestor script completed.")
