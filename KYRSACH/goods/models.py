from django.db import models
from main.models import CustomUser

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Size(models.Model):
    size = models.CharField(max_length=10)

    def __str__(self):
        return self.size

class Color(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sizes = models.ManyToManyField(Size)
    colors = models.ManyToManyField(Color)
    is_new = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    size = models.ForeignKey(Size, on_delete=models.SET_NULL, null=True)
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.product} - {self.quantity} pcs'

class Cart(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem)

    def __str__(self):
        return f'Cart of {self.user.username}'

class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('Processing', 'Processing'), ('Shipped', 'Shipped')])

    def __str__(self):
        return f'Order {self.id} by {self.user.username}'


class Purchase(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    user = models.ForeignKey('main.CustomUser', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product.name} - {self.user.email}'