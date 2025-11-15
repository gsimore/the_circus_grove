# The Circus Grove

A full-stack monorepo application for tracking training, nutrition, and personal check-ins. Built with Django 5, Django REST Framework, Vue 3, and modern web technologies.

## 🎪 Features

- **User Authentication**: JWT-based authentication with access and refresh tokens
- **Training Management**: Track workout sessions, exercises, sets, reps, and intensity
- **Nutrition Tracking**: Log meals, food items, macros, and calories
- **Daily Check-ins**: Monitor weight, body composition, mood, energy levels, and sleep
- **Mobile-First Design**: Responsive UI built with Tailwind CSS
- **RESTful API**: Comprehensive API with OpenAPI/Swagger documentation

## 🛠️ Tech Stack

### Backend
- Django 5.0
- Django REST Framework
- JWT Authentication (Simple JWT)
- PostgreSQL
- drf-spectacular (OpenAPI/Swagger)
- Docker

### Frontend
- Vue 3
- Vite
- Pinia (State Management)
- Vue Router
- Axios
- Tailwind CSS
- Docker

## 🚀 Quick Start

### Prerequisites
- Docker and Docker Compose
- Git

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/gsimore/the_circus_grove.git
cd the_circus_grove
```

2. **Copy environment variables**
```bash
cp .env.example .env
```

3. **Start the application with Docker Compose**
```bash
docker compose up --build
```

The services will be available at:
- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/api/docs/
- **Django Admin**: http://localhost:8000/admin/

### Initial Setup

1. **Run migrations**
```bash
docker compose exec backend python manage.py migrate
```

2. **Create a superuser**
```bash
docker compose exec backend python manage.py createsuperuser
```

## 📁 Project Structure

```
the_circus_grove/
├── backend/              # Django backend
│   ├── circus_grove/     # Main Django project
│   ├── users/            # User management app
│   ├── training/         # Training sessions app
│   ├── nutrition/        # Nutrition tracking app
│   ├── checkins/         # Daily check-ins app
│   ├── requirements.txt  # Python dependencies
│   └── Dockerfile
├── frontend/             # Vue 3 frontend
│   ├── src/
│   │   ├── api/         # API client and endpoints
│   │   ├── stores/      # Pinia stores
│   │   ├── router/      # Vue Router config
│   │   ├── views/       # Vue components/views
│   │   └── main.js
│   ├── package.json
│   └── Dockerfile
├── docker-compose.yml    # Docker Compose configuration
├── .env.example          # Environment variables template
└── README.md
```

## 🔧 Development

### Backend Development

**Without Docker:**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

**Run tests:**
```bash
python manage.py test
```

### Frontend Development

**Without Docker:**
```bash
cd frontend
npm install
npm run dev
```

**Build for production:**
```bash
npm run build
```

## 📚 API Endpoints

### Authentication
- `POST /api/auth/token/` - Obtain JWT token pair
- `POST /api/auth/token/refresh/` - Refresh access token
- `POST /api/users/register/` - Register new user
- `GET /api/users/profile/` - Get user profile
- `PATCH /api/users/profile/` - Update user profile

### Training
- `GET /api/training/sessions/` - List training sessions
- `POST /api/training/sessions/` - Create training session
- `GET /api/training/sessions/{id}/` - Get session details
- `PATCH /api/training/sessions/{id}/` - Update session
- `DELETE /api/training/sessions/{id}/` - Delete session
- `GET /api/training/sessions/{id}/exercises/` - List exercises
- `POST /api/training/sessions/{id}/exercises/` - Add exercise

### Nutrition
- `GET /api/nutrition/meals/` - List meals
- `POST /api/nutrition/meals/` - Create meal
- `GET /api/nutrition/meals/{id}/` - Get meal details
- `PATCH /api/nutrition/meals/{id}/` - Update meal
- `DELETE /api/nutrition/meals/{id}/` - Delete meal
- `GET /api/nutrition/meals/{id}/foods/` - List food items
- `POST /api/nutrition/meals/{id}/foods/` - Add food item

### Check-ins
- `GET /api/checkins/` - List check-ins
- `POST /api/checkins/` - Create check-in
- `GET /api/checkins/{id}/` - Get check-in details
- `PATCH /api/checkins/{id}/` - Update check-in
- `DELETE /api/checkins/{id}/` - Delete check-in

## 🔐 Environment Variables

### Backend
- `DEBUG` - Debug mode (default: True)
- `SECRET_KEY` - Django secret key
- `DATABASE_URL` - PostgreSQL connection URL
- `ALLOWED_HOSTS` - Allowed host names
- `CORS_ALLOWED_ORIGINS` - CORS allowed origins

### Frontend
- `VITE_API_URL` - Backend API URL (default: http://localhost:8000)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License.

## 👤 Author

**gsimore**

- GitHub: [@gsimore](https://github.com/gsimore)
