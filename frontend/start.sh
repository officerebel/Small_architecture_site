#!/bin/bash

echo "🚀 Starting Frontend Server..."

# Ensure we're using the built files
if [ ! -d "dist" ]; then
    echo "❌ No dist folder found. Running build..."
    npm run build
fi

# Start the server
PORT=${PORT:-3000}
echo "🌐 Starting server on port $PORT"
npx serve dist -s -p $PORT