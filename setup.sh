#!/bin/bash

# Setup script for The Circus Grove

echo "🎪 Setting up The Circus Grove..."

# Check if .env exists
if [ ! -f .env ]; then
    echo "📝 Creating .env file from .env.example..."
    cp .env.example .env
fi

echo "✅ Environment file ready"
echo ""
echo "🐳 Starting Docker containers..."
docker-compose up -d

echo ""
echo "⏳ Waiting for database to be ready..."
sleep 10

echo ""
echo "🔄 Running database migrations..."
docker-compose exec -T backend python manage.py migrate

echo ""
echo "📦 Collecting static files..."
docker-compose exec -T backend python manage.py collectstatic --noinput

echo ""
echo "✅ Setup complete!"
echo ""
echo "🌐 Services are available at:"
echo "   Frontend:        http://localhost:5173"
echo "   Backend API:     http://localhost:8000"
echo "   API Docs:        http://localhost:8000/api/docs/"
echo "   Admin Panel:     http://localhost:8000/admin/"
echo ""
echo "📝 To create a superuser, run:"
echo "   docker-compose exec backend python manage.py createsuperuser"
