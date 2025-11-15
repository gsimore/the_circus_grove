from rest_framework import serializers
from .models import Meal, Food, NutritionPlan, NutritionPlanMeal


class FoodSerializer(serializers.ModelSerializer):
    """Serializer for Food model."""
    
    class Meta:
        model = Food
        fields = ['id', 'name', 'quantity', 'calories', 'protein_g', 'carbs_g', 'fat_g']


class MealSerializer(serializers.ModelSerializer):
    """Serializer for Meal model."""
    foods = FoodSerializer(many=True, read_only=True)
    user = serializers.StringRelatedField(read_only=True)
    nutrition_plan_name = serializers.CharField(source='nutrition_plan.name', read_only=True)
    
    class Meta:
        model = Meal
        fields = [
            'id', 'user', 'nutrition_plan', 'nutrition_plan_name', 'name', 'meal_type', 'date', 'time',
            'calories', 'protein_g', 'carbs_g', 'fat_g',
            'notes', 'foods', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']


class MealCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating meals with foods."""
    foods = FoodSerializer(many=True, required=False)
    
    class Meta:
        model = Meal
        fields = [
            'nutrition_plan', 'name', 'meal_type', 'date', 'time',
            'calories', 'protein_g', 'carbs_g', 'fat_g',
            'notes', 'foods'
        ]

    def create(self, validated_data):
        foods_data = validated_data.pop('foods', [])
        meal = Meal.objects.create(**validated_data)
        
        for food_data in foods_data:
            Food.objects.create(meal=meal, **food_data)
        
        return meal


class NutritionPlanMealSerializer(serializers.ModelSerializer):
    """Serializer for NutritionPlanMeal model."""
    meal_type_display = serializers.CharField(source='get_meal_type_display', read_only=True)
    
    class Meta:
        model = NutritionPlanMeal
        fields = [
            'id', 'meal_type', 'meal_type_display', 'scheduled_time',
            'target_calories', 'target_protein_g', 'target_carbs_g', 'target_fat_g',
            'is_pre_workout', 'is_post_workout', 'notes', 'order',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class NutritionPlanSerializer(serializers.ModelSerializer):
    """Serializer for NutritionPlan model."""
    meals = NutritionPlanMealSerializer(many=True, read_only=True)
    coach_username = serializers.CharField(source='coach.username', read_only=True)
    user_username = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = NutritionPlan
        fields = [
            'id', 'coach', 'coach_username', 'user', 'user_username',
            'name', 'description', 'target_calories', 'target_protein_g',
            'target_carbs_g', 'target_fat_g', 'start_date', 'end_date',
            'is_active', 'meals', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'coach', 'created_at', 'updated_at']


class NutritionPlanCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating nutrition plans with meals."""
    meals = NutritionPlanMealSerializer(many=True, required=False)
    
    class Meta:
        model = NutritionPlan
        fields = [
            'user', 'name', 'description', 'target_calories', 'target_protein_g',
            'target_carbs_g', 'target_fat_g', 'start_date', 'end_date',
            'is_active', 'meals'
        ]

    def create(self, validated_data):
        meals_data = validated_data.pop('meals', [])
        # Set coach from request user
        validated_data['coach'] = self.context['request'].user
        plan = NutritionPlan.objects.create(**validated_data)
        
        for meal_data in meals_data:
            NutritionPlanMeal.objects.create(plan=plan, **meal_data)
        
        return plan
