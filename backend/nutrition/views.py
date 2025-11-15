from rest_framework import generics, permissions
from .models import Meal, Food
from .serializers import MealSerializer, MealCreateSerializer, FoodSerializer


class MealListCreateView(generics.ListCreateAPIView):
    """View for listing and creating meals."""
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Meal.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return MealCreateSerializer
        return MealSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MealDetailView(generics.RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating, and deleting a meal."""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = MealSerializer

    def get_queryset(self):
        return Meal.objects.filter(user=self.request.user)


class FoodListCreateView(generics.ListCreateAPIView):
    """View for listing and creating foods."""
    serializer_class = FoodSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        meal_id = self.kwargs.get('meal_id')
        return Food.objects.filter(meal_id=meal_id, meal__user=self.request.user)

    def perform_create(self, serializer):
        meal_id = self.kwargs.get('meal_id')
        meal = Meal.objects.get(id=meal_id, user=self.request.user)
        serializer.save(meal=meal)

