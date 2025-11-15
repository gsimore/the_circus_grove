from rest_framework import serializers
from .models import Meal, Food


class FoodSerializer(serializers.ModelSerializer):
    """Serializer for Food model."""
    
    class Meta:
        model = Food
        fields = ['id', 'name', 'quantity', 'calories', 'protein_g', 'carbs_g', 'fat_g']


class MealSerializer(serializers.ModelSerializer):
    """Serializer for Meal model."""
    foods = FoodSerializer(many=True, read_only=True)
    user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Meal
        fields = [
            'id', 'user', 'name', 'meal_type', 'date', 'time',
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
            'name', 'meal_type', 'date', 'time',
            'calories', 'protein_g', 'carbs_g', 'fat_g',
            'notes', 'foods'
        ]

    def create(self, validated_data):
        foods_data = validated_data.pop('foods', [])
        meal = Meal.objects.create(**validated_data)
        
        for food_data in foods_data:
            Food.objects.create(meal=meal, **food_data)
        
        return meal
