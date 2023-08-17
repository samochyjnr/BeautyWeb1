from django.shortcuts import render
from .models import Product

def home(request):
    record = Product.objects.all()
    return render(request, 'apps/home.html', {'record':record})

def index(request):
    return render(request, 'apps/index.html', {})