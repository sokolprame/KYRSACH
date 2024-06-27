from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from main.forms import PurchaseForm
from .forms import ProductForm, PurchaseForm

def catalog(request):
    products = Product.objects.all()
    return render(request, 'goods/catalog.html', {'products': products})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'main/catalog.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    form = PurchaseForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        purchase = form.save(commit=False)
        purchase.product = product
        purchase.user = request.user
        purchase.save()
        return redirect('goods:product_detail', product_id=product.id)
    return render(request, 'main/product_detail.html', {'product': product, 'form': form})

@login_required
def purchase(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            purchase = form.save(commit=False)
            purchase.user = request.user
            purchase.product = product
            purchase.save()
            return redirect('goods:product_list')
    else:
        form = PurchaseForm(initial={'product': product})
    return render(request, 'goods/purchase.html', {'form': form, 'product': product})
