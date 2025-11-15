from rest_framework import generics, permissions
from django.shortcuts import get_object_or_404
from .models import TrainingSession, Exercise, TrainingPlan, TrainingPlanExercise
from .serializers import (
    TrainingSessionSerializer,
    TrainingSessionCreateSerializer,
    ExerciseSerializer,
    TrainingPlanSerializer,
    TrainingPlanCreateSerializer,
    TrainingPlanExerciseSerializer
)


class TrainingSessionListCreateView(generics.ListCreateAPIView):
    """View for listing and creating training sessions."""
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return TrainingSession.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TrainingSessionCreateSerializer
        return TrainingSessionSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TrainingSessionDetailView(generics.RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating, and deleting a training session."""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TrainingSessionSerializer

    def get_queryset(self):
        return TrainingSession.objects.filter(user=self.request.user)


class ExerciseListCreateView(generics.ListCreateAPIView):
    """View for listing and creating exercises."""
    serializer_class = ExerciseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        session_id = self.kwargs.get('session_id')
        return Exercise.objects.filter(session_id=session_id, session__user=self.request.user)

    def perform_create(self, serializer):
        session_id = self.kwargs.get('session_id')
        session = TrainingSession.objects.get(id=session_id, user=self.request.user)
        serializer.save(session=session)


class TrainingPlanListCreateView(generics.ListCreateAPIView):
    """View for listing and creating training plans."""
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.user_type == 'coach':
            # Coaches can see plans they created
            return TrainingPlan.objects.filter(coach=user)
        else:
            # Normal users can see their own plans
            return TrainingPlan.objects.filter(user=user)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TrainingPlanCreateSerializer
        return TrainingPlanSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def perform_create(self, serializer):
        # Coach is set in serializer from request.user
        serializer.save()


class TrainingPlanDetailView(generics.RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating, and deleting a training plan."""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TrainingPlanSerializer

    def get_queryset(self):
        user = self.request.user
        if user.user_type == 'coach':
            return TrainingPlan.objects.filter(coach=user)
        else:
            return TrainingPlan.objects.filter(user=user)


class TrainingPlanExerciseListCreateView(generics.ListCreateAPIView):
    """View for listing and creating exercises in a training plan."""
    serializer_class = TrainingPlanExerciseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        plan_id = self.kwargs.get('plan_id')
        user = self.request.user
        # Ensure user has access to the plan
        if user.user_type == 'coach':
            plan = get_object_or_404(TrainingPlan, id=plan_id, coach=user)
        else:
            plan = get_object_or_404(TrainingPlan, id=plan_id, user=user)
        return TrainingPlanExercise.objects.filter(plan=plan)

    def perform_create(self, serializer):
        plan_id = self.kwargs.get('plan_id')
        user = self.request.user
        if user.user_type == 'coach':
            plan = get_object_or_404(TrainingPlan, id=plan_id, coach=user)
        else:
            plan = get_object_or_404(TrainingPlan, id=plan_id, user=user)
        serializer.save(plan=plan)

