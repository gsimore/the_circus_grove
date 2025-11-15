from django.db import models
from django.conf import settings


class CheckIn(models.Model):
    """Model for user check-ins."""
    MOOD_CHOICES = [
        ('excellent', 'Excellent'),
        ('good', 'Good'),
        ('neutral', 'Neutral'),
        ('poor', 'Poor'),
        ('bad', 'Bad'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='checkins')
    date = models.DateField()
    weight_kg = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    body_fat_percentage = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    muscle_mass_kg = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    mood = models.CharField(max_length=20, choices=MOOD_CHOICES, blank=True, null=True)
    energy_level = models.PositiveSmallIntegerField(blank=True, null=True)  # 1-10 scale
    sleep_hours = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    water_intake_ml = models.PositiveIntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'checkins'
        ordering = ['-date', '-created_at']
        unique_together = ['user', 'date']

    def __str__(self):
        return f"{self.user.username} - {self.date}"

