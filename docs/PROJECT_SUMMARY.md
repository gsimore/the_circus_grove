# The Circus Grove - Project Summary

## Overview

The Circus Grove is a comprehensive full-stack application for fitness tracking, designed to help users monitor their training sessions, nutrition intake, and daily check-ins. Built with modern web technologies and containerized with Docker for easy deployment.

## Architecture

### Monorepo Structure
```
the_circus_grove/
├── backend/     # Django 4.2 + DRF API
├── frontend/    # Vue 3 + Vite SPA
├── docs/        # API and development documentation
└── docker-compose.yml
```

## Technology Stack

### Backend (Django 4.2 + DRF)
- **Framework**: Django 4.2 LTS
- **API**: Django REST Framework 3.14
- **Authentication**: JWT (djangorestframework-simplejwt 5.3.1)
- **Database**: PostgreSQL 15
- **Documentation**: drf-spectacular (OpenAPI/Swagger)
- **Features**:
  - Custom User model with extended profile
  - Token-based authentication with refresh
  - RESTful API endpoints
  - Admin interface
  - CORS enabled for frontend

### Frontend (Vue 3 + Vite)
- **Framework**: Vue 3.5 (Composition API)
- **Build Tool**: Vite 7.2
- **State Management**: Pinia 3.0
- **Routing**: Vue Router 4.6
- **HTTP Client**: Axios 1.13
- **Styling**: Tailwind CSS 3.x
- **Features**:
  - JWT token management with auto-refresh
  - Mobile-first responsive design
  - Protected routes with navigation guards
  - Centralized API layer
  - Modular store architecture

### Database Models

#### Users App
- Custom User model extending AbstractUser
- Fields: username, email, phone, bio, date_of_birth, height_cm
- JWT authentication support

#### Training App
- **TrainingSession**: Track workouts with date, duration, intensity, calories
- **Exercise**: Individual exercises with sets, reps, weight, rest periods
- Relationship: One session has many exercises

#### Nutrition App
- **Meal**: Track meals with type (breakfast/lunch/dinner/snack), date, macros
- **Food**: Individual food items with quantity and nutritional information
- Relationship: One meal has many foods

#### Check-ins App
- **CheckIn**: Daily check-ins tracking:
  - Weight and body composition
  - Mood and energy levels
  - Sleep hours and water intake
  - Progress notes
- Unique constraint: one check-in per user per day

## API Endpoints

### Authentication
- `POST /api/auth/token/` - Login and obtain JWT tokens
- `POST /api/auth/token/refresh/` - Refresh access token
- `POST /api/users/register/` - User registration
- `GET /api/users/profile/` - Get current user profile
- `PATCH /api/users/profile/` - Update user profile

### Training
- `GET/POST /api/training/sessions/` - List/create training sessions
- `GET/PATCH/DELETE /api/training/sessions/{id}/` - Session operations
- `GET/POST /api/training/sessions/{id}/exercises/` - Exercise operations

### Nutrition
- `GET/POST /api/nutrition/meals/` - List/create meals
- `GET/PATCH/DELETE /api/nutrition/meals/{id}/` - Meal operations
- `GET/POST /api/nutrition/meals/{id}/foods/` - Food operations

### Check-ins
- `GET/POST /api/checkins/` - List/create check-ins
- `GET/PATCH/DELETE /api/checkins/{id}/` - Check-in operations

### Documentation
- `GET /api/docs/` - Interactive Swagger UI
- `GET /api/schema/` - OpenAPI schema

## Frontend Routes

- `/login` - User login (guest only)
- `/register` - User registration (guest only)
- `/dashboard` - Main dashboard (protected)
- `/training` - Training sessions list (protected)
- `/training/:id` - Session details (protected)
- `/nutrition` - Meals list (protected)
- `/nutrition/:id` - Meal details (protected)
- `/checkins` - Check-ins list (protected)
- `/profile` - User profile (protected)

## Docker Services

### Database (PostgreSQL)
- Image: postgres:15-alpine
- Port: 5432
- Volume: postgres_data (persistent)
- Health check enabled

### Backend (Django)
- Custom Dockerfile
- Port: 8000
- Volume mount for hot-reload development
- Depends on: database
- Auto-runs migrations on start

### Frontend (Vue/Vite)
- Custom Dockerfile with Node 20
- Port: 5173
- Volume mount for hot-reload development
- Depends on: backend
- Dev server with HMR

## Key Features

### Security
- JWT authentication with access/refresh tokens
- Token auto-refresh on expiration
- CORS protection
- CSRF protection
- Password hashing
- Protected routes

### User Experience
- Mobile-first responsive design
- Clean, modern UI with Tailwind CSS
- Loading states and error handling
- Intuitive navigation
- Real-time form validation

### Developer Experience
- Makefile with common commands
- Setup script for quick start
- Comprehensive documentation
- Docker Compose for easy deployment
- Hot-reload in development
- Type safety with Pinia stores
- Modular, maintainable code structure

## Getting Started

```bash
# Quick start
make setup

# Or manually
cp .env.example .env
docker compose up -d
docker compose exec backend python manage.py migrate
docker compose exec backend python manage.py createsuperuser
```

## Services URLs

- Frontend: http://localhost:5173
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/api/docs/
- Admin: http://localhost:8000/admin/

## Project Statistics

- **Backend**: 4 Django apps, 7 models, 15+ API endpoints
- **Frontend**: 10+ Vue components, 4 Pinia stores, 10+ routes
- **Documentation**: 2 comprehensive guides (API + Development)
- **Configuration**: Docker Compose, Makefiles, environment templates

## Future Enhancements

Potential additions:
- Analytics and progress charts
- Social features (sharing workouts)
- Meal planning and recipes
- Exercise library with videos
- Mobile app (React Native/Flutter)
- Real-time notifications
- Integration with fitness trackers
- AI-powered recommendations

## License

MIT License

## Author

Built by gsimore for The Circus Grove
