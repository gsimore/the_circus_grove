from rest_framework import serializers
from .models import TrainingSession, Exercise, TrainingPlan, TrainingPlanExercise


class ExerciseSerializer(serializers.ModelSerializer):
    """Serializer for Exercise model."""
    
    class Meta:
        model = Exercise
        fields = ['id', 'name', 'sets', 'reps', 'weight_kg', 'rest_seconds', 'notes']


class TrainingSessionSerializer(serializers.ModelSerializer):
    """Serializer for TrainingSession model."""
    exercises = ExerciseSerializer(many=True, read_only=True)
    user = serializers.StringRelatedField(read_only=True)
    training_plan_name = serializers.CharField(source='training_plan.name', read_only=True)
    
    class Meta:
        model = TrainingSession
        fields = [
            'id', 'user', 'training_plan', 'training_plan_name', 'title', 'description', 'date',
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
            'training_plan', 'title', 'description', 'date', 'duration_minutes',
            'intensity', 'calories_burned', 'notes', 'exercises'
        ]

    def create(self, validated_data):
        exercises_data = validated_data.pop('exercises', [])
        session = TrainingSession.objects.create(**validated_data)
        
        for exercise_data in exercises_data:
            Exercise.objects.create(session=session, **exercise_data)
        
        return session


class TrainingPlanExerciseSerializer(serializers.ModelSerializer):
    """Serializer for TrainingPlanExercise model."""
    day_of_week_display = serializers.CharField(source='get_day_of_week_display', read_only=True)
    
    class Meta:
        model = TrainingPlanExercise
        fields = [
            'id', 'exercise_name', 'day_of_week', 'day_of_week_display',
            'scheduled_date', 'sets', 'reps', 'weight_kg', 'rest_seconds',
            'order', 'notes', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class TrainingPlanSerializer(serializers.ModelSerializer):
    """Serializer for TrainingPlan model."""
    exercises = TrainingPlanExerciseSerializer(many=True, read_only=True)
    coach_username = serializers.CharField(source='coach.username', read_only=True)
    user_username = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = TrainingPlan
        fields = [
            'id', 'coach', 'coach_username', 'user', 'user_username',
            'name', 'description', 'start_date', 'end_date', 'is_active',
            'exercises', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'coach', 'created_at', 'updated_at']


class TrainingPlanCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating training plans with exercises."""
    exercises = TrainingPlanExerciseSerializer(many=True, required=False)
    
    class Meta:
        model = TrainingPlan
        fields = [
            'user', 'name', 'description', 'start_date', 'end_date',
            'is_active', 'exercises'
        ]

    def create(self, validated_data):
        exercises_data = validated_data.pop('exercises', [])
        # Set coach from request user
        validated_data['coach'] = self.context['request'].user
        plan = TrainingPlan.objects.create(**validated_data)
        
        for exercise_data in exercises_data:
            TrainingPlanExercise.objects.create(plan=plan, **exercise_data)
        
        return plan
