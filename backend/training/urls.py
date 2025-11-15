from django.urls import path
from .views import (
    TrainingSessionListCreateView,
    TrainingSessionDetailView,
    ExerciseListCreateView,
    TrainingPlanListCreateView,
    TrainingPlanDetailView,
    TrainingPlanExerciseListCreateView
)

app_name = 'training'

urlpatterns = [
    path('sessions/', TrainingSessionListCreateView.as_view(), name='session-list'),
    path('sessions/<int:pk>/', TrainingSessionDetailView.as_view(), name='session-detail'),
    path('sessions/<int:session_id>/exercises/', ExerciseListCreateView.as_view(), name='exercise-list'),
    path('plans/', TrainingPlanListCreateView.as_view(), name='plan-list'),
    path('plans/<int:pk>/', TrainingPlanDetailView.as_view(), name='plan-detail'),
    path('plans/<int:plan_id>/exercises/', TrainingPlanExerciseListCreateView.as_view(), name='plan-exercise-list'),
]
