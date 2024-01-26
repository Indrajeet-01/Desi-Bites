from django.db import models

class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ('starter', 'Starter'),
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('drinks', 'Drinks'),
        ('desserts', 'Desserts'),
        ('fast_food', 'Fast Food'),
    ]
    name = models.CharField(max_length = 255)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

# Create your models here.
