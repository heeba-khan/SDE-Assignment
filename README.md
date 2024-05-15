# Log Control System

## Overview

This project is aimed at building a log control system that captures logs from different stages using APIs and provides a query interface to search and filter these logs efficiently.

## Running the Project

### Prerequisites

- Python 3.x installed on your system
- Internet connection (for API mock calls)

### Steps

1. Clone the repository:

   ```sh
   git clone https://github.com/heeba-khan/SDE-Assignment.git

2. Navigate to the project directory:
   
   ```sh
   cd SDE-Assignment

3. Install the required Python packages:

   ```sh
   pip install -r requirements.txt

4. Run the log ingestor script to generate log files:

    ```sh
    python log_ingestor.py

5. Run the query interface script to query the logs:

    ```sh
    python query_interface.py --level error


## System Design

The system consists of two main components:

- Log Ingestor: Responsible for capturing logs from different stages using mock APIs and writing them to log files.
- Query Interface: Provides a user interface (CLI) for searching and filtering logs based on various criteria.
  

## Log Ingestor

- Integrates mock APIs to capture logs at different stages.
- Standardizes log format and writes logs to designated log files.
- Configures logging levels and file paths for each API.

  
## Implements error handling to ensure robustness.

- Query Interface
- Offers a CLI for full-text search across logs.
- Includes filters based on level, log string, timestamp, and source.
- Provides efficient and quick search results.

## Features Implemented

- Log Ingestor:

  - Integration with mock APIs.
  - Standardized log formatting.
  - Logging configuration.
  - Error handling.

- Query Interface:

  - Full-text search.
  - Filters based on level, log string, timestamp, and source.

## Identified Issues

  - Empty log files: Occasionally, log files may be created but remain empty due to errors in logging or API integration. This issue needs further investigation and debugging.






