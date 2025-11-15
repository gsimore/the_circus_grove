# The Circus Grove API Documentation

This document provides detailed information about The Circus Grove REST API.

## Base URL

```
http://localhost:8000/api
```

## Authentication

The API uses JWT (JSON Web Token) authentication. To authenticate:

1. Obtain tokens by sending credentials to `/api/auth/token/`
2. Include the access token in the Authorization header: `Authorization: Bearer <token>`
3. Refresh expired tokens using `/api/auth/token/refresh/`

### Authentication Endpoints

#### Obtain Token
```http
POST /api/auth/token/
Content-Type: application/json

{
  "username": "your_username",
  "password": "your_password"
}
```

**Response:**
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

#### Refresh Token
```http
POST /api/auth/token/refresh/
Content-Type: application/json

{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

**Response:**
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

## User Management

### Register
```http
POST /api/users/register/
Content-Type: application/json

{
  "username": "newuser",
  "email": "user@example.com",
  "password": "securepassword",
  "password_confirm": "securepassword",
  "first_name": "John",
  "last_name": "Doe"
}
```

### Get Profile
```http
GET /api/users/profile/
Authorization: Bearer <token>
```

### Update Profile
```http
PATCH /api/users/profile/
Authorization: Bearer <token>
Content-Type: application/json

{
  "first_name": "John",
  "last_name": "Doe",
  "bio": "Fitness enthusiast",
  "phone": "+1234567890",
  "date_of_birth": "1990-01-01",
  "height_cm": 175.5
}
```

## Training Sessions

### List Training Sessions
```http
GET /api/training/sessions/
Authorization: Bearer <token>
```

### Create Training Session
```http
POST /api/training/sessions/
Authorization: Bearer <token>
Content-Type: application/json

{
  "title": "Morning Workout",
  "description": "Full body workout",
  "date": "2024-01-15",
  "duration_minutes": 60,
  "intensity": "high",
  "calories_burned": 500,
  "notes": "Felt great today",
  "exercises": [
    {
      "name": "Bench Press",
      "sets": 4,
      "reps": 10,
      "weight_kg": 80.0,
      "rest_seconds": 90,
      "notes": "Good form"
    },
    {
      "name": "Squats",
      "sets": 4,
      "reps": 12,
      "weight_kg": 100.0,
      "rest_seconds": 120
    }
  ]
}
```

### Get Training Session Details
```http
GET /api/training/sessions/{id}/
Authorization: Bearer <token>
```

### Update Training Session
```http
PATCH /api/training/sessions/{id}/
Authorization: Bearer <token>
Content-Type: application/json

{
  "title": "Updated Workout",
  "notes": "Added extra sets"
}
```

### Delete Training Session
```http
DELETE /api/training/sessions/{id}/
Authorization: Bearer <token>
```

### Add Exercise to Session
```http
POST /api/training/sessions/{session_id}/exercises/
Authorization: Bearer <token>
Content-Type: application/json

{
  "name": "Deadlift",
  "sets": 3,
  "reps": 8,
  "weight_kg": 120.0,
  "rest_seconds": 180
}
```

## Nutrition

### List Meals
```http
GET /api/nutrition/meals/
Authorization: Bearer <token>
```

### Create Meal
```http
POST /api/nutrition/meals/
Authorization: Bearer <token>
Content-Type: application/json

{
  "name": "Breakfast",
  "meal_type": "breakfast",
  "date": "2024-01-15",
  "time": "08:00:00",
  "calories": 500,
  "protein_g": 30.0,
  "carbs_g": 60.0,
  "fat_g": 15.0,
  "notes": "Post-workout meal",
  "foods": [
    {
      "name": "Oatmeal",
      "quantity": "1 cup",
      "calories": 300,
      "protein_g": 10.0,
      "carbs_g": 50.0,
      "fat_g": 5.0
    },
    {
      "name": "Banana",
      "quantity": "1 medium",
      "calories": 105,
      "protein_g": 1.3,
      "carbs_g": 27.0,
      "fat_g": 0.4
    }
  ]
}
```

### Get Meal Details
```http
GET /api/nutrition/meals/{id}/
Authorization: Bearer <token>
```

### Update Meal
```http
PATCH /api/nutrition/meals/{id}/
Authorization: Bearer <token>
Content-Type: application/json

{
  "calories": 550,
  "notes": "Added protein shake"
}
```

### Delete Meal
```http
DELETE /api/nutrition/meals/{id}/
Authorization: Bearer <token>
```

## Check-ins

### List Check-ins
```http
GET /api/checkins/
Authorization: Bearer <token>
```

### Create Check-in
```http
POST /api/checkins/
Authorization: Bearer <token>
Content-Type: application/json

{
  "date": "2024-01-15",
  "weight_kg": 75.5,
  "body_fat_percentage": 15.5,
  "muscle_mass_kg": 60.0,
  "mood": "good",
  "energy_level": 8,
  "sleep_hours": 7.5,
  "water_intake_ml": 2500,
  "notes": "Feeling strong today"
}
```

### Get Check-in Details
```http
GET /api/checkins/{id}/
Authorization: Bearer <token>
```

### Update Check-in
```http
PATCH /api/checkins/{id}/
Authorization: Bearer <token>
Content-Type: application/json

{
  "weight_kg": 75.3,
  "notes": "Weight slightly down"
}
```

### Delete Check-in
```http
DELETE /api/checkins/{id}/
Authorization: Bearer <token>
```

## Response Formats

### Success Response
```json
{
  "id": 1,
  "field": "value",
  ...
}
```

### List Response
```json
{
  "count": 100,
  "next": "http://localhost:8000/api/endpoint/?page=2",
  "previous": null,
  "results": [
    {...},
    {...}
  ]
}
```

### Error Response
```json
{
  "detail": "Error message"
}
```

or

```json
{
  "field_name": ["Error message for this field"]
}
```

## Status Codes

- `200 OK` - Request successful
- `201 Created` - Resource created successfully
- `204 No Content` - Resource deleted successfully
- `400 Bad Request` - Invalid request data
- `401 Unauthorized` - Authentication required or invalid token
- `403 Forbidden` - Permission denied
- `404 Not Found` - Resource not found
- `500 Internal Server Error` - Server error

## Pagination

List endpoints support pagination with the following query parameters:

- `page` - Page number (default: 1)
- `page_size` - Items per page (default: 20, max: 100)

Example:
```
GET /api/training/sessions/?page=2&page_size=10
```

## Interactive API Documentation

Visit http://localhost:8000/api/docs/ for interactive Swagger UI documentation where you can test all endpoints.
