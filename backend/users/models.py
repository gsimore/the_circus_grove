from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError


class User(AbstractUser):
    """Custom user model for The Circus Grove."""
    USER_TYPE_CHOICES = [
        ('normal', 'Normal User'),
        ('coach', 'Coach'),
    ]

    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    height_cm = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='normal')
    coach = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='clients',
        limit_choices_to={'user_type': 'coach'}
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'
        ordering = ['-created_at']

    def clean(self):
        """Validate that only normal users can have a coach."""
        if self.coach and self.user_type != 'normal':
            raise ValidationError("Only normal users can be assigned a coach.")
        if self.coach and self.coach.user_type != 'coach':
            raise ValidationError("The assigned coach must be a coach user type.")
        if self.coach and self.coach == self:
            raise ValidationError("A user cannot be their own coach.")

    def save(self, *args, **kwargs):
        """Override save to call clean validation."""
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username

