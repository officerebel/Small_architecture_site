#!/bin/bash

echo "🚀 Setting up local development environment..."

# Start PostgreSQL with Docker
echo "📦 Starting PostgreSQL with Docker..."
docker-compose up -d postgres

# Wait for PostgreSQL to be ready
echo "⏳ Waiting for PostgreSQL to be ready..."
sleep 10

# Activate virtual environment
echo "🐍 Activating virtual environment..."
source backend/venv/bin/activate

# Install Python dependencies
echo "📚 Installing Python dependencies..."
cd backend
pip install -r requirements.txt

# Run migrations
echo "🔄 Running database migrations..."
python manage.py migrate

# Create initial data
echo "📝 Setting up initial data..."
python manage.py setup_initial_data

# Collect static files
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput

echo "✅ Local setup complete!"
echo ""
echo "🌐 To start the development servers:"
echo "   Backend:  cd backend && python manage.py runserver 8002"
echo "   Frontend: cd frontend && npm run dev"
echo ""
echo "🔗 URLs:"
echo "   Backend API: http://localhost:8002/api/"
echo "   Admin Panel: http://localhost:8002/cms/"
echo "   Frontend:    http://localhost:9000"
echo ""
echo "👤 Admin credentials: admin / changeme123"