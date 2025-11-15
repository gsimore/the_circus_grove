from rest_framework import serializers
from .models import TrainingSession, Exercise


class ExerciseSerializer(serializers.ModelSerializer):
    """Serializer for Exercise model."""
    
    class Meta:
        model = Exercise
        fields = ['id', 'name', 'sets', 'reps', 'weight_kg', 'rest_seconds', 'notes']


class TrainingSessionSerializer(serializers.ModelSerializer):
    """Serializer for TrainingSession model."""
    exercises = ExerciseSerializer(many=True, read_only=True)
    user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = TrainingSession
        fields = [
            'id', 'user', 'title', 'description', 'date',
            'duration_minutes', 'intensity', 'calories_burned',
            'notes', 'exercises', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']


class TrainingSessionCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating training sessions with exercises."""
    exercises = ExerciseSerializer(many=True, required=False)
    
    class Meta:
        model = TrainingSession
        fields = [
            'title', 'description', 'date', 'duration_minutes',
            'intensity', 'calories_burned', 'notes', 'exercises'
        ]

    def create(self, validated_data):
        exercises_data = validated_data.pop('exercises', [])
        session = TrainingSession.objects.create(**validated_data)
        
        for exercise_data in exercises_data:
            Exercise.objects.create(session=session, **exercise_data)
        
        return session
