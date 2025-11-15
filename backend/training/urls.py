from django.urls import path
from .views import (
    TrainingSessionListCreateView,
    TrainingSessionDetailView,
    ExerciseListCreateView
)

app_name = 'training'

urlpatterns = [
    path('sessions/', TrainingSessionListCreateView.as_view(), name='session-list'),
    path('sessions/<int:pk>/', TrainingSessionDetailView.as_view(), name='session-detail'),
    path('sessions/<int:session_id>/exercises/', ExerciseListCreateView.as_view(), name='exercise-list'),
]
