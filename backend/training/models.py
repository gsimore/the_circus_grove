from django.db import models
from django.conf import settings


class TrainingSession(models.Model):
    """Model for training sessions."""
    INTENSITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='training_sessions')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()
    duration_minutes = models.PositiveIntegerField()
    intensity = models.CharField(max_length=10, choices=INTENSITY_CHOICES)
    calories_burned = models.PositiveIntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'training_sessions'
        ordering = ['-date', '-created_at']

    def __str__(self):
        return f"{self.title} - {self.date}"


class Exercise(models.Model):
    """Model for exercises in a training session."""
    session = models.ForeignKey(TrainingSession, on_delete=models.CASCADE, related_name='exercises')
    name = models.CharField(max_length=200)
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()
    weight_kg = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    rest_seconds = models.PositiveIntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'exercises'
        ordering = ['id']

    def __str__(self):
        return f"{self.name} - {self.sets}x{self.reps}"

