#!/bin/bash

echo "🚀 Deploying Frontend to Vercel..."

# Install Vercel CLI if not present
if ! command -v vercel &> /dev/null; then
    echo "📦 Installing Vercel CLI..."
    npm install -g vercel
fi

# Navigate to frontend directory
cd frontend

# Build the project
echo "🔨 Building frontend..."
npm run build

# Deploy to Vercel
echo "🌐 Deploying to Vercel..."
vercel --prod

echo "✅ Frontend deployment complete!"
echo ""
echo "🔗 Your sites:"
echo "   Backend API: https://smallachitecture-production.up.railway.app/api/v2/pages/"
echo "   Admin Panel: https://smallachitecture-production.up.railway.app/cms/"
echo "   Frontend: Check Vercel output above"