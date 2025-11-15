from django.db import models
from django.conf import settings


class Meal(models.Model):
    """Model for meals."""
    MEAL_TYPE_CHOICES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('snack', 'Snack'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='meals')
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

