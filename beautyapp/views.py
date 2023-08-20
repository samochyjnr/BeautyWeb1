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

def checkout(request):
    return render(request, 'apps/checkout.html', {})

def blog(request):
    return render(request, 'apps/blog.html', {})

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        return render(request, 'apps/contact.html', {'name':name})
    else:
        return render(request, 'apps/contact.html', {})



    