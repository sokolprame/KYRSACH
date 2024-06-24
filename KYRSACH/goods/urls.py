from django.urls import path
from .views import product_list, product_detail, purchase

urlpatterns = [
    path('', product_list, name='product_list'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
    path('purchase/<int:pk>/', purchase, name='purchase'),
]
