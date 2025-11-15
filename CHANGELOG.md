# Changelog

All notable changes to The Circus Grove project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial monorepo setup for The Circus Grove application
- Django 5.0 backend with Django REST Framework
- Vue 3 frontend with Vite build tool
- JWT authentication system with access and refresh tokens
- PostgreSQL database integration
- Docker Compose configuration for full-stack development
- User management with custom User model
- Training sessions tracking with exercise details
- Nutrition tracking with meals and food items
- Daily check-ins for progress monitoring
- RESTful API with comprehensive endpoints
- OpenAPI/Swagger documentation
- Mobile-first responsive design with Tailwind CSS
- Pinia state management
- Vue Router with protected routes
- API client layer with Axios
- Comprehensive documentation (API, Development, Contributing)
- Makefile with common development commands
- Setup script for quick start
- Environment configuration templates

### Backend Features
- Custom User model with extended profile fields (phone, bio, date_of_birth, height_cm)
- TrainingSession model with duration, intensity, calories tracking
- Exercise model with sets, reps, weight, rest periods
- Meal model with meal types and nutritional macros
- Food model for individual food items
- CheckIn model for daily progress tracking (weight, body composition, mood, energy, sleep)
- JWT authentication endpoints
- User registration and profile management endpoints
- CRUD endpoints for training sessions
- CRUD endpoints for meals and nutrition
- CRUD endpoints for check-ins
- Django admin interface for all models
- CORS configuration for frontend
- drf-spectacular for OpenAPI schema generation

### Frontend Features
- Vue 3 Composition API
- Pinia stores for auth, training, nutrition, and check-ins
- JWT token management with automatic refresh
- Login and registration forms
- Dashboard with navigation
- Protected route guards
- Axios interceptors for auth token injection
- Mobile-first Tailwind CSS styling
- Component structure for all major features
- API client modules for each backend service

### DevOps
- Docker Compose setup with 3 services (db, backend, frontend)
- PostgreSQL 15 Alpine image
- Backend Dockerfile with Python 3.11
- Frontend Dockerfile with Node 20
- Volume persistence for database
- Hot-reload for development
- Health checks for database service
- Environment variable configuration

### Documentation
- Comprehensive README with quick start guide
- API documentation with example requests/responses
- Development guide with coding standards
- Project summary document
- Contributing guidelines
- Makefile reference
- Setup script documentation

## [0.1.0] - 2024-11-15

### Initial Release
- Project scaffolding and structure
- Core backend and frontend implementation
- Docker containerization
- Complete documentation

---

## Legend

- `Added` - New features
- `Changed` - Changes in existing functionality
- `Deprecated` - Soon-to-be removed features
- `Removed` - Removed features
- `Fixed` - Bug fixes
- `Security` - Security improvements
