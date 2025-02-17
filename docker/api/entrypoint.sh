#!/bin/bash

# Wait for the PostgreSQL database to be ready
until pg_isready -h db -p 5432; do
  echo "Waiting for the database to be ready..."
  sleep 1
done

# Run alembic migrations
alembic upgrade head

# Start the application
uvicorn api.main:app --host 0.0.0.0 --port 8000 --reload