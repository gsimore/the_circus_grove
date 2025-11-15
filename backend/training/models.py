from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError


class TrainingPlan(models.Model):
    """Model for training plans created by coaches for users."""
    coach = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='created_training_plans',
        limit_choices_to={'user_type': 'coach'}
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='training_plans',
        limit_choices_to={'user_type': 'normal'}
    )
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'training_plans'
        ordering = ['-created_at']
        unique_together = [['user', 'name']]

    def clean(self):
        """Validate that coach is actually a coach and user is a normal user."""
        if self.coach.user_type != 'coach':
            raise ValidationError("The coach must be a coach user type.")
        if self.user.user_type != 'normal':
            raise ValidationError("The user must be a normal user type.")
        if self.end_date and self.end_date < self.start_date:
            raise ValidationError("End date must be after start date.")

    def save(self, *args, **kwargs):
        """Override save to call clean validation."""
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.user.username}"


class TrainingPlanExercise(models.Model):
    """Model for exercises scheduled in a training plan."""
    DAY_OF_WEEK_CHOICES = [
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday'),
        (5, 'Saturday'),
        (6, 'Sunday'),
    ]

    plan = models.ForeignKey(TrainingPlan, on_delete=models.CASCADE, related_name='exercises')
    exercise_name = models.CharField(max_length=200)
    day_of_week = models.IntegerField(choices=DAY_OF_WEEK_CHOICES, blank=True, null=True)
    scheduled_date = models.DateField(blank=True, null=True)
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()
    weight_kg = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    rest_seconds = models.PositiveIntegerField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0, help_text="Order within the day")
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'training_plan_exercises'
        ordering = ['day_of_week', 'order', 'id']

    def clean(self):
        """Validate that either day_of_week or scheduled_date is provided."""
        if not self.day_of_week and not self.scheduled_date:
            raise ValidationError("Either day_of_week or scheduled_date must be provided.")

    def save(self, *args, **kwargs):
        """Override save to call clean validation."""
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        day = self.get_day_of_week_display() if self.day_of_week is not None else str(self.scheduled_date)
        return f"{self.exercise_name} - {day}"


class TrainingSession(models.Model):
    """Model for training sessions."""
    INTENSITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='training_sessions')
    training_plan = models.ForeignKey(
        TrainingPlan,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='sessions'
    )
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

