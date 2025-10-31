#!/usr/bin/env python
"""
Portfolio Site - Django/Wagtail Application
Entry point for Railway deployment
Updated: 2025-10-31
"""

import os
import sys
import subprocess
import time

def run_command(cmd, description):
    """Run a command with error handling"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed:")
        print(f"Error: {e.stderr}")
        return False

def main():
    """Main entry point for the application"""
    print("🚀 Starting Portfolio Site deployment...")
    
    # Change to backend directory
    os.chdir('backend')
    
    # Set Django settings module
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_site.settings')
    
    # Wait a moment for database to be ready
    print("⏳ Waiting for database to be ready...")
    time.sleep(5)
    
    # Run migrations
    if not run_command(['python', 'manage.py', 'migrate'], 'Database migration'):
        print("⚠️ Migration failed, but continuing...")
    
    # Setup initial data
    run_command(['python', 'manage.py', 'setup_initial_data'], 'Initial data setup')
    
    # Collect static files
    run_command(['python', 'manage.py', 'collectstatic', '--noinput'], 'Static files collection')
    
    # Start the server
    print("🌐 Starting Django server...")
    port = os.environ.get('PORT', '8000')
    subprocess.run([
        'gunicorn', 
        'portfolio_site.wsgi:application',
        '--bind', f'0.0.0.0:{port}',
        '--workers', '2',
        '--timeout', '120'
    ], check=True)

if __name__ == '__main__':
    main()