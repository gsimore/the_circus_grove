from rest_framework import generics, permissions
from django.shortcuts import get_object_or_404
from .models import Meal, Food, NutritionPlan, NutritionPlanMeal
from .serializers import (
    MealSerializer, MealCreateSerializer, FoodSerializer,
    NutritionPlanSerializer, NutritionPlanCreateSerializer,
    NutritionPlanMealSerializer
)


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


class NutritionPlanListCreateView(generics.ListCreateAPIView):
    """View for listing and creating nutrition plans."""
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.user_type == 'coach':
            # Coaches can see plans they created
            return NutritionPlan.objects.filter(coach=user)
        else:
            # Normal users can see their own plans
            return NutritionPlan.objects.filter(user=user)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return NutritionPlanCreateSerializer
        return NutritionPlanSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def perform_create(self, serializer):
        # Coach is set in serializer from request.user
        serializer.save()


class NutritionPlanDetailView(generics.RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating, and deleting a nutrition plan."""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NutritionPlanSerializer

    def get_queryset(self):
        user = self.request.user
        if user.user_type == 'coach':
            return NutritionPlan.objects.filter(coach=user)
        else:
            return NutritionPlan.objects.filter(user=user)


class NutritionPlanMealListCreateView(generics.ListCreateAPIView):
    """View for listing and creating meals in a nutrition plan."""
    serializer_class = NutritionPlanMealSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        plan_id = self.kwargs.get('plan_id')
        user = self.request.user
        # Ensure user has access to the plan
        if user.user_type == 'coach':
            plan = get_object_or_404(NutritionPlan, id=plan_id, coach=user)
        else:
            plan = get_object_or_404(NutritionPlan, id=plan_id, user=user)
        return NutritionPlanMeal.objects.filter(plan=plan)

    def perform_create(self, serializer):
        plan_id = self.kwargs.get('plan_id')
        user = self.request.user
        if user.user_type == 'coach':
            plan = get_object_or_404(NutritionPlan, id=plan_id, coach=user)
        else:
            plan = get_object_or_404(NutritionPlan, id=plan_id, user=user)
        serializer.save(plan=plan)

