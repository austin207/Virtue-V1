#!/bin/bash
# backend/scripts/start.sh
# Startup script for the backend service

# Uncomment the next line if using a virtual environment
# source venv/bin/activate

# Load environment variables from .env file
export $(grep -v '^#' ../.env | xargs)

# (Optional) Run database migrations using Alembic
# alembic upgrade head

# Start the FastAPI application using Uvicorn
uvicorn app.main:app --host 0.0.0.0 --port 8000
