from rest_framework import generics, permissions
from .models import TrainingSession, Exercise
from .serializers import (
    TrainingSessionSerializer,
    TrainingSessionCreateSerializer,
    ExerciseSerializer
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

