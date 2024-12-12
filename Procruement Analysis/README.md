# Procruement Analysis

## Overview
The Procruement Analysis project is designed to streamline and analyze procurement data efficiently. The project is structured to ensure scalability, modularity, and ease of use.

## Project Structure

```
Procruement Analysis/
│
├── .env              # Environment variables file
├── .idea/            # IDE configuration files (optional)
└── app/              # Main application directory
    ├── src/          # Source code for the application
    │   ├── agents/   # Modules for managing AI agents
    │   ├── ai_service/   # AI service-related logic
    │   ├── database_conf/   # Database configurations and connections
    │   ├── models/   # Data models (e.g., ORM models)
    │   ├── routers/  # API route definitions
    │   └── service/  # Business logic modules
    │
    └── utils/        # Utility modules
        ├── constants/    # Constant definitions
        ├── logging/      # Logging configuration
        ├── exceptions/   # Custom exceptions
        └── prompts/      # AI prompts or templates
```

## Setup Instructions

### Prerequisites
- Python 3.8+
- Pip (Python package manager)
- Virtual Environment (optional but recommended)

### Installation Steps

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Procruement Analysis
   ```

2. Set up a virtual environment (optional):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables:
   - Copy the `.env` template and update it with your credentials and settings:
     ```bash
     cp .env.example .env
     ```

5. Run the application:
   ```bash
   python main.py
   ```

## Features

- **AI Service Integration**: Provides AI-driven insights for procurement data.
- **Database Configuration**: Modular setup for managing database connections.
- **API Routes**: Predefined API routes for interacting with the system.
- **Logging and Error Handling**: Centralized logging and custom exception handling.
- **Environment Configurations**: Easily configurable using `.env`.

## Folder Descriptions

### `src`
- **agents**: Manages AI agents for task automation.
- **ai_service**: Handles AI/ML-related services.
- **database_conf**: Includes database connection configurations and setup.
- **models**: Defines data models, typically for ORM (e.g., SQLAlchemy).
- **routers**: API route definitions for the project.
- **service**: Contains business logic and service-related code.

### `utils`
- **constants**: Centralized location for defining project constants.
- **logging**: Configuration files and utilities for project logging.
- **exceptions**: Custom exception definitions for error handling.
- **prompts**: Stores templates or prompts used in AI services.

