from django.db import models
from django.core.validators import RegexValidator

class Reservation(models.Model):
    name = models.CharField(max_length=255)
    
    phone = models.CharField(max_length=10,validators=[RegexValidator(r'^\d{10}$', message='Phone number must be 10 digits')])

    date = models.DateField()
    time = models.CharField(max_length=255, blank=True)
    guests = models.PositiveIntegerField()
    message = models.TextField(blank=True)

    def __str__(self):
        return self.name




# Create your models here.
