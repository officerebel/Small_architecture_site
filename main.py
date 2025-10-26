#!/usr/bin/env python
"""
Portfolio Site - Django/Wagtail Application
Entry point for Railway deployment
"""

import os
import sys
import subprocess

def main():
    """Main entry point for the application"""
    # Change to backend directory
    os.chdir('backend')
    
    # Set Django settings module
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_site.settings')
    
    # Run migrations
    subprocess.run(['poetry', 'run', 'python', 'manage.py', 'migrate'], check=True)
    
    # Collect static files
    subprocess.run(['poetry', 'run', 'python', 'manage.py', 'collectstatic', '--noinput'], check=True)
    
    # Start the server
    port = os.environ.get('PORT', '8000')
    subprocess.run([
        'poetry', 'run', 'gunicorn', 
        'portfolio_site.wsgi:application',
        '--bind', f'0.0.0.0:{port}'
    ], check=True)

if __name__ == '__main__':
    main()