from django.shortcuts import render
from .models import Product, Category

def home(request):
    record = Product.objects.all()
    return render(request, 'apps/home.html', {'record':record})

def index(request):
    cat = Category.objects.all()
    return render(request, 'apps/index.html', {'cat':cat})