from rest_framework import serializers
from .models import CheckIn


class CheckInSerializer(serializers.ModelSerializer):
    """Serializer for CheckIn model."""
    user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = CheckIn
        fields = [
            'id', 'user', 'date', 'weight_kg', 'body_fat_percentage',
            'muscle_mass_kg', 'mood', 'energy_level', 'sleep_hours',
            'water_intake_ml', 'notes', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']
