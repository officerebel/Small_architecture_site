#!/bin/bash

echo "🚀 Deploying Frontend to Railway..."

# Navigate to frontend directory
cd frontend

# Install serve dependency
echo "📦 Installing serve dependency..."
npm install serve

# Build the project
echo "🔨 Building frontend with Vite..."
npm run build

# Check if build was successful
if [ ! -d "dist" ]; then
    echo "❌ Build failed - dist directory not found"
    exit 1
fi

echo "✅ Frontend build complete!"
echo "📁 Built files are in frontend/dist/"
echo ""
echo "🌐 To deploy to Railway:"
echo "1. Connect to your frontend Railway project"
echo "2. Push this repository to trigger deployment"
echo "3. Railway will use nixpacks.toml to build and serve the frontend"
echo ""
echo "🔗 Your backend API: https://smallachitecture-production.up.railway.app/api/v2/pages/"