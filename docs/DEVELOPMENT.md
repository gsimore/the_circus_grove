# Development Guide

This guide covers development workflows, best practices, and common tasks for The Circus Grove project.

## Getting Started

### Prerequisites

- Docker Desktop (recommended) or Docker + Docker Compose
- Git
- Node.js 20+ (for local frontend development)
- Python 3.11+ (for local backend development)

### Initial Setup

1. Clone the repository:
```bash
git clone https://github.com/gsimore/the_circus_grove.git
cd the_circus_grove
```

2. Run the setup script:
```bash
make setup
# or
./setup.sh
```

3. Create a superuser for admin access:
```bash
make createsuperuser
```

## Development Workflow

### Using Docker (Recommended)

**Start services:**
```bash
make up
# or
docker-compose up -d
```

**View logs:**
```bash
make logs
# or
docker-compose logs -f
```

**Stop services:**
```bash
make down
# or
docker-compose down
```

### Backend Development

**Local development without Docker:**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

**Create migrations:**
```bash
make makemigrations
# or
docker-compose exec backend python manage.py makemigrations
```

**Run migrations:**
```bash
make migrate
# or
docker-compose exec backend python manage.py migrate
```

**Django shell:**
```bash
make shell
# or
docker-compose exec backend python manage.py shell
```

**Run tests:**
```bash
make test
# or
docker-compose exec backend python manage.py test
```

### Frontend Development

**Local development without Docker:**
```bash
cd frontend
npm install
npm run dev
```

**Build for production:**
```bash
cd frontend
npm run build
```

**Preview production build:**
```bash
cd frontend
npm run preview
```

## Project Structure

### Backend Structure

```
backend/
├── circus_grove/          # Django project settings
│   ├── settings.py        # Main settings
│   ├── urls.py            # Root URL configuration
│   ├── wsgi.py            # WSGI application
│   └── asgi.py            # ASGI application
├── users/                 # User management
│   ├── models.py          # User model
│   ├── serializers.py     # User serializers
│   ├── views.py           # User views
│   ├── urls.py            # User URLs
│   └── admin.py           # Admin configuration
├── training/              # Training management
├── nutrition/             # Nutrition tracking
├── checkins/              # Daily check-ins
├── manage.py              # Django management script
└── requirements.txt       # Python dependencies
```

### Frontend Structure

```
frontend/
├── src/
│   ├── api/              # API client layer
│   │   ├── client.js     # Axios instance with interceptors
│   │   ├── auth.js       # Auth endpoints
│   │   ├── training.js   # Training endpoints
│   │   ├── nutrition.js  # Nutrition endpoints
│   │   └── checkins.js   # Check-in endpoints
│   ├── stores/           # Pinia state management
│   │   ├── auth.js       # Auth store
│   │   ├── training.js   # Training store
│   │   ├── nutrition.js  # Nutrition store
│   │   └── checkins.js   # Check-ins store
│   ├── router/           # Vue Router
│   │   └── index.js      # Route definitions
│   ├── views/            # Page components
│   │   ├── auth/         # Authentication pages
│   │   ├── training/     # Training pages
│   │   ├── nutrition/    # Nutrition pages
│   │   └── checkins/     # Check-in pages
│   ├── components/       # Reusable components
│   ├── App.vue           # Root component
│   └── main.js           # Application entry point
├── package.json          # Node dependencies
└── vite.config.js        # Vite configuration
```

## Coding Standards

### Python (Backend)

- Follow PEP 8 style guide
- Use meaningful variable and function names
- Write docstrings for classes and functions
- Keep functions small and focused
- Use type hints where appropriate

**Example:**
```python
def create_training_session(user: User, data: dict) -> TrainingSession:
    """Create a new training session for a user.
    
    Args:
        user: The user creating the session
        data: Session data dictionary
        
    Returns:
        TrainingSession: The created session instance
    """
    session = TrainingSession.objects.create(user=user, **data)
    return session
```

### JavaScript/Vue (Frontend)

- Use ES6+ features
- Follow Vue 3 Composition API style
- Use meaningful variable and function names
- Keep components small and focused
- Use TypeScript for complex logic (optional)

**Example:**
```javascript
// Composition API style
import { ref, onMounted } from 'vue'

export default {
  setup() {
    const sessions = ref([])
    const loading = ref(false)
    
    const fetchSessions = async () => {
      loading.value = true
      try {
        const response = await trainingApi.getSessions()
        sessions.value = response.data
      } catch (error) {
        console.error('Failed to fetch sessions:', error)
      } finally {
        loading.value = false
      }
    }
    
    onMounted(() => {
      fetchSessions()
    })
    
    return {
      sessions,
      loading,
      fetchSessions,
    }
  }
}
```

## Common Tasks

### Adding a New Model

1. Define model in `models.py`
2. Create migrations: `make makemigrations`
3. Run migrations: `make migrate`
4. Create serializer in `serializers.py`
5. Create views in `views.py`
6. Add URLs in `urls.py`
7. Register in `admin.py`

### Adding a New API Endpoint

**Backend:**
1. Create view function or class in `views.py`
2. Add URL pattern in `urls.py`
3. Update serializers if needed

**Frontend:**
1. Add API method in appropriate file under `src/api/`
2. Update store if needed in `src/stores/`
3. Create or update view component

### Database Management

**Reset database:**
```bash
make clean
make setup
```

**Create database backup:**
```bash
docker-compose exec db pg_dump -U circus_user circus_grove > backup.sql
```

**Restore database:**
```bash
cat backup.sql | docker-compose exec -T db psql -U circus_user circus_grove
```

## Testing

### Backend Tests

Create tests in each app's `tests.py`:

```python
from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class UserModelTests(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.assertEqual(user.username, 'testuser')
        self.assertTrue(user.check_password('testpass123'))
```

Run tests:
```bash
make test
```

### Frontend Tests

(To be implemented - add testing framework like Vitest)

## Environment Variables

### Backend (.env)

```bash
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=postgresql://user:password@db:5432/dbname
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:5173
```

### Frontend (.env)

```bash
VITE_API_URL=http://localhost:8000
```

## Troubleshooting

### Backend Issues

**Migrations conflict:**
```bash
docker-compose exec backend python manage.py migrate --fake-initial
```

**Clear all migrations:**
```bash
# Delete migration files (except __init__.py)
# Then:
make makemigrations
make migrate
```

### Frontend Issues

**Clear node_modules:**
```bash
cd frontend
rm -rf node_modules package-lock.json
npm install
```

**Port already in use:**
```bash
# Change port in docker-compose.yml or kill process using the port
lsof -ti:5173 | xargs kill -9
```

### Docker Issues

**Rebuild containers:**
```bash
make build
make up
```

**Clean everything:**
```bash
make clean
docker system prune -a
make setup
```

## Contributing

1. Create a feature branch: `git checkout -b feature/my-feature`
2. Make your changes
3. Write tests
4. Ensure all tests pass
5. Commit with clear message: `git commit -m "Add feature X"`
6. Push to your fork: `git push origin feature/my-feature`
7. Create a Pull Request

## Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Vue 3 Documentation](https://vuejs.org/)
- [Pinia Documentation](https://pinia.vuejs.org/)
- [Tailwind CSS](https://tailwindcss.com/)
