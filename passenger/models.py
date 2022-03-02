from django.db import models
from django.forms import CharField

# Create your models here.

class Passenger(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)

    class Meta:
        db_table = 'passenger'