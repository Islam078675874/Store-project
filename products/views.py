from django.shortcuts import render
from .models import Product

def home(request):
    return render(request,'products/home.html')

def product_list(request):
    products = Product.objects.all()
    return render(request,'products/list.html',{'products':products})
