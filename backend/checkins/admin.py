from django.contrib import admin
from .models import CheckIn


@admin.register(CheckIn)
class CheckInAdmin(admin.ModelAdmin):
    """Admin for CheckIn model."""
    list_display = ['user', 'date', 'weight_kg', 'mood', 'energy_level', 'created_at']
    list_filter = ['mood', 'date', 'created_at']
    search_fields = ['user__username', 'notes']
    ordering = ['-date', '-created_at']

