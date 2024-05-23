from unittest.util import _MAX_LENGTH
from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=10)

class UserUpdate(models.Model):
    
    def __str__(self):
        return f'{self.title} {self.size}'