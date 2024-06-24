from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/', default='https://example.com/path/to/default/image.jpg')  # ƒобавл€ем поле image с значением по умолчанию

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    card_number = models.CharField(max_length=20)
    expiration_date = models.CharField(max_length=5)
    cvv = models.CharField(max_length=4)
