from django.shortcuts import render
from .models import Product, Category

def home(request):
    record = Product.objects.all()
    return render(request, 'apps/home.html', {'record':record})

def about(request):
    cat = Category.objects.all()
    return render(request, 'apps/about.html', {'cat':cat})

def product(request):
    return render(request, 'apps/product.html', {})

def product_single(request):
    return render(request, 'apps/product_single.html', {})

def cart(request):
    return render(request, 'apps/cart.html', {})
    