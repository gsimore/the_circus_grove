from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError


class NutritionPlan(models.Model):
    """Model for nutrition plans created by coaches for users."""
    coach = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='created_nutrition_plans',
        limit_choices_to={'user_type': 'coach'}
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='nutrition_plans',
        limit_choices_to={'user_type': 'normal'}
    )
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    target_calories = models.PositiveIntegerField()
    target_protein_g = models.DecimalField(max_digits=6, decimal_places=2)
    target_carbs_g = models.DecimalField(max_digits=6, decimal_places=2)
    target_fat_g = models.DecimalField(max_digits=6, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'nutrition_plans'
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


class NutritionPlanMeal(models.Model):
    """Model for meal timings and targets within a nutrition plan."""
    MEAL_TYPE_CHOICES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('snack', 'Snack'),
        ('pre_workout', 'Pre-Workout'),
        ('post_workout', 'Post-Workout'),
    ]

    plan = models.ForeignKey(NutritionPlan, on_delete=models.CASCADE, related_name='meals')
    meal_type = models.CharField(max_length=20, choices=MEAL_TYPE_CHOICES)
    scheduled_time = models.TimeField(help_text="Recommended time to consume this meal")
    target_calories = models.PositiveIntegerField(blank=True, null=True)
    target_protein_g = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    target_carbs_g = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    target_fat_g = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    is_pre_workout = models.BooleanField(default=False, help_text="Meal should be consumed before training")
    is_post_workout = models.BooleanField(default=False, help_text="Meal should be consumed after training")
    notes = models.TextField(blank=True, null=True, help_text="Guidance on meal timing and composition")
    order = models.PositiveIntegerField(default=0, help_text="Order of meal within the day")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'nutrition_plan_meals'
        ordering = ['scheduled_time', 'order', 'id']
        unique_together = [['plan', 'meal_type', 'scheduled_time']]

    def __str__(self):
        return f"{self.get_meal_type_display()} - {self.scheduled_time} ({self.plan.name})"


class Meal(models.Model):
    """Model for meals."""
    MEAL_TYPE_CHOICES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('snack', 'Snack'),
        ('pre_workout', 'Pre-Workout'),
        ('post_workout', 'Post-Workout'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='meals')
    nutrition_plan = models.ForeignKey(
        NutritionPlan,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='tracked_meals'
    )
    name = models.CharField(max_length=200)
    meal_type = models.CharField(max_length=20, choices=MEAL_TYPE_CHOICES)
    date = models.DateField()
    time = models.TimeField(blank=True, null=True)
    calories = models.PositiveIntegerField()
    protein_g = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    carbs_g = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    fat_g = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'meals'
        ordering = ['-date', '-created_at']

    def __str__(self):
        return f"{self.name} - {self.date}"


class Food(models.Model):
    """Model for food items in a meal."""
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='foods')
    name = models.CharField(max_length=200)
    quantity = models.CharField(max_length=100)
    calories = models.PositiveIntegerField()
    protein_g = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    carbs_g = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    fat_g = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    class Meta:
        db_table = 'foods'
        ordering = ['id']

    def __str__(self):
        return f"{self.name} - {self.quantity}"

