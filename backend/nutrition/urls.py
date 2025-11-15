from django.urls import path
from .views import MealListCreateView, MealDetailView, FoodListCreateView

app_name = 'nutrition'

urlpatterns = [
    path('meals/', MealListCreateView.as_view(), name='meal-list'),
    path('meals/<int:pk>/', MealDetailView.as_view(), name='meal-detail'),
    path('meals/<int:meal_id>/foods/', FoodListCreateView.as_view(), name='food-list'),
]
