from django.contrib import admin
from .models import Meal, Food


class FoodInline(admin.TabularInline):
    """Inline admin for foods."""
    model = Food
    extra = 1


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    """Admin for Meal model."""
    list_display = ['name', 'user', 'meal_type', 'date', 'calories', 'created_at']
    list_filter = ['meal_type', 'date', 'created_at']
    search_fields = ['name', 'user__username']
    ordering = ['-date', '-created_at']
    inlines = [FoodInline]

