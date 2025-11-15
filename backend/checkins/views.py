from rest_framework import generics, permissions
from .models import CheckIn
from .serializers import CheckInSerializer


class CheckInListCreateView(generics.ListCreateAPIView):
    """View for listing and creating check-ins."""
    serializer_class = CheckInSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CheckIn.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CheckInDetailView(generics.RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating, and deleting a check-in."""
    serializer_class = CheckInSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CheckIn.objects.filter(user=self.request.user)

