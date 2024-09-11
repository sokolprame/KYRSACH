from django.urls import path
from . import views

app_name = 'goods'

urlpatterns = [
    path('catalog/', views.catalog, name='catalog'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('add_to_cart/<int:variant_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('order_success/', views.order_success, name='order_success'),
    path('add_to_wishlist/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('account/', views.account, name='account'),
]