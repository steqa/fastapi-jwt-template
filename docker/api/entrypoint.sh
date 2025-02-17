#!/bin/bash

# Wait for the PostgreSQL database to be ready
until pg_isready -h db -p 5432; do
  echo "Waiting for the database to be ready..."
  sleep 1
done

# Generate an RSA private key, of size 2048
if [ ! -f /app/api/auth/certs/jwt-private.pem ]; then
  echo "Generating private key..."
  openssl genrsa -out /app/api/auth/certs/jwt-private.pem 2048
fi


# Extract the public key from the key pair, which can be used in a certificate
if [ ! -f /app/api/auth/certs/jwt-public.pem ]; then
  echo "Generating public key..."
  openssl rsa -in /app/api/auth/certs/jwt-private.pem -outform PEM -pubout -out /app/api/auth/certs/jwt-public.pem
fi


# Generate a 32-byte random secret key encoded in base64
if [ ! -f /app/api/user/certs/secret.key ]; then
  echo "Generating secret key..."
  openssl rand -base64 32 > /app/api/user/certs/secret.key
fi

# Run alembic migrations
echo "Running alembic migrations..."
alembic upgrade head

# Start the application
uvicorn api.main:app --host 0.0.0.0 --port 8000 --reload