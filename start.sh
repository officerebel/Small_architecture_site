#!/bin/bash

# Install dependencies with Poetry
poetry config virtualenvs.create false
poetry install --only=main --no-dev

# Check if we're in the root directory or backend directory
if [ -f "backend/manage.py" ]; then
    cd backend
fi

# Run migrations
poetry run python manage.py migrate

# Collect static files
poetry run python manage.py collectstatic --noinput

# Start the server
poetry run gunicorn portfolio_site.wsgi:application --bind 0.0.0.0:$PORT