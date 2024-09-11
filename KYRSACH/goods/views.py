from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product, ProductVariant, Cart, Order, Wishlist
from .forms import ProductForm, ProductVariantForm

def catalog(request):
    products = Product.objects.all()
    return render(request, 'goods/catalog.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    variants = ProductVariant.objects.filter(product=product)
    similar_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]
    return render(request, 'goods/product_detail.html', {
        'product': product,
        'variants': variants,
        'similar_products': similar_products
    })

@login_required
def add_to_cart(request, variant_id):
    variant = get_object_or_404(ProductVariant, id=variant_id)
    cart, created = Cart.objects.get_or_create(user=request.user, product_variant=variant)
    if not created:
        cart.quantity += 1
        cart.save()
    return redirect('goods:cart')

@login_required
def cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.product_variant.product.price * item.quantity for item in cart_items)
    return render(request, 'goods/cart.html', {'cart_items': cart_items, 'total_price': total_price})

@login_required
def checkout(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.product_variant.product.price * item.quantity for item in cart_items)
    if request.method == 'POST':
        order = Order.objects.create(user=request.user, total_price=total_price)
        for item in cart_items:
            order.products.add(item.product_variant)
        cart_items.delete()
        return redirect('goods:order_success')
    return render(request, 'goods/checkout.html', {'cart_items': cart_items, 'total_price': total_price})

def order_success(request):
    return render(request, 'goods/order_success.html')

@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Wishlist.objects.get_or_create(user=request.user, product=product)
    return redirect('goods:wishlist')

@login_required
def wishlist(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, 'goods/wishlist.html', {'wishlist_items': wishlist_items})

@login_required
def account(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'goods/account.html', {'orders': orders})