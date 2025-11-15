from django.contrib import admin
from .models import TrainingSession, Exercise


class ExerciseInline(admin.TabularInline):
    """Inline admin for exercises."""
    model = Exercise
    extra = 1


@admin.register(TrainingSession)
class TrainingSessionAdmin(admin.ModelAdmin):
    """Admin for TrainingSession model."""
    list_display = ['title', 'user', 'date', 'duration_minutes', 'intensity', 'created_at']
    list_filter = ['intensity', 'date', 'created_at']
    search_fields = ['title', 'user__username', 'description']
    ordering = ['-date', '-created_at']
    inlines = [ExerciseInline]

