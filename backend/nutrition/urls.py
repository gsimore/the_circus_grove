from django.urls import path
from .views import (
    MealListCreateView, MealDetailView, FoodListCreateView,
    NutritionPlanListCreateView, NutritionPlanDetailView,
    NutritionPlanMealListCreateView
)

app_name = 'nutrition'

urlpatterns = [
    path('meals/', MealListCreateView.as_view(), name='meal-list'),
    path('meals/<int:pk>/', MealDetailView.as_view(), name='meal-detail'),
    path('meals/<int:meal_id>/foods/', FoodListCreateView.as_view(), name='food-list'),
    path('plans/', NutritionPlanListCreateView.as_view(), name='plan-list'),
    path('plans/<int:pk>/', NutritionPlanDetailView.as_view(), name='plan-detail'),
    path('plans/<int:plan_id>/meals/', NutritionPlanMealListCreateView.as_view(), name='plan-meal-list'),
]
