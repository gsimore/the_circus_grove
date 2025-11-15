from django.contrib import admin
from .models import Meal, Food, NutritionPlan, NutritionPlanMeal


class FoodInline(admin.TabularInline):
    """Inline admin for foods."""
    model = Food
    extra = 1


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    """Admin for Meal model."""
    list_display = ['name', 'user', 'nutrition_plan', 'meal_type', 'date', 'calories', 'created_at']
    list_filter = ['meal_type', 'date', 'created_at']
    search_fields = ['name', 'user__username']
    ordering = ['-date', '-created_at']
    inlines = [FoodInline]


class NutritionPlanMealInline(admin.TabularInline):
    """Inline admin for nutrition plan meals."""
    model = NutritionPlanMeal
    extra = 1


@admin.register(NutritionPlan)
class NutritionPlanAdmin(admin.ModelAdmin):
    """Admin for NutritionPlan model."""
    list_display = ['name', 'coach', 'user', 'target_calories', 'start_date', 'end_date', 'is_active', 'created_at']
    list_filter = ['is_active', 'start_date', 'created_at']
    search_fields = ['name', 'coach__username', 'user__username', 'description']
    ordering = ['-created_at']
    inlines = [NutritionPlanMealInline]

