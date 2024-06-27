# goods/urls.py
from django.urls import path
from .views import product_list, product_detail, purchase, catalog

app_name = 'goods'

urlpatterns = [
    path('', product_list, name='product_list'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
    path('purchase/', purchase, name='purchase'),
    path('catalog/', catalog, name='catalog'),
]
