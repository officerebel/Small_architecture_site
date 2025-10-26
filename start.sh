#!/bin/bash

# Check if we're in the root directory or backend directory
if [ -f "backend/manage.py" ]; then
    cd backend
fi

# Install dependencies
pip install -r requirements-prod.txt

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Start the server
gunicorn portfolio_site.wsgi:application --bind 0.0.0.0:$PORT