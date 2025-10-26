#!/usr/bin/env python
"""
Initialize database for Railway deployment
"""
import os
import sys
import django
from django.core.management import execute_from_command_line

# Add backend to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_site.settings')

# Setup Django
django.setup()

# Run migrations
execute_from_command_line(['manage.py', 'migrate'])

# Create initial data
execute_from_command_line(['manage.py', 'setup_initial_data'])

print("✅ Database initialized successfully!")