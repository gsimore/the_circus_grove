from django.contrib import admin
from .models import TrainingSession, Exercise, TrainingPlan, TrainingPlanExercise


class ExerciseInline(admin.TabularInline):
    """Inline admin for exercises."""
    model = Exercise
    extra = 1


@admin.register(TrainingSession)
class TrainingSessionAdmin(admin.ModelAdmin):
    """Admin for TrainingSession model."""
    list_display = ['title', 'user', 'training_plan', 'date', 'duration_minutes', 'intensity', 'created_at']
    list_filter = ['intensity', 'date', 'created_at']
    search_fields = ['title', 'user__username', 'description']
    ordering = ['-date', '-created_at']
    inlines = [ExerciseInline]


class TrainingPlanExerciseInline(admin.TabularInline):
    """Inline admin for training plan exercises."""
    model = TrainingPlanExercise
    extra = 1


@admin.register(TrainingPlan)
class TrainingPlanAdmin(admin.ModelAdmin):
    """Admin for TrainingPlan model."""
    list_display = ['name', 'coach', 'user', 'start_date', 'end_date', 'is_active', 'created_at']
    list_filter = ['is_active', 'start_date', 'created_at']
    search_fields = ['name', 'coach__username', 'user__username', 'description']
    ordering = ['-created_at']
    inlines = [TrainingPlanExerciseInline]

