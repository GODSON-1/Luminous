import random
from django.shortcuts import  render
from . models import Product
from django.core.paginator import Paginator  # noqa: F401
# Create your views here.
def index(request):
    new_products = Product.objects.all().order_by('-created_at')[:6]  # noqa: F841
    return render(request,'index.html',{'new_products':new_products})

def blog_page(request):
    return render(request, 'blog_page.html')

def list_products(request):
    
    page=1
    if request.GET:
        page=request.GET.get('page',1)
        
    product_list=Product.objects.order_by('priority')  # noqa: F841
    product_paginator=Paginator(product_list,8)  # noqa: F841
    product_list=product_paginator.get_page(page)
    return render(request,'products.html',{'hide_blog_and_contact':True , "products": product_list})


def detail_product(request,pk):
    product=Product.objects.get(pk=pk) # noqa: F841
    other_products = list(Product.objects.exclude(id=pk))  # noqa: F841
    random.shuffle(other_products)  # noqa: F841
    randomized_products = [product] + other_products[:6]
    
    context = {
        'product': product,
        'products': randomized_products,
    }
    return render(request, 'product_detail.html',context)


def mens_products(request):
    page = request.GET.get('page', 1)
    product_list = Product.objects.filter(priority=1).order_by('?')  # Random order for variety
    paginator = Paginator(product_list, 8)
    products = paginator.get_page(page)
    return render(request, 'products.html', {
        'products': products,
        'current_collection': 'men'
    })

def womens_products(request):
    page = request.GET.get('page', 1)
    product_list = Product.objects.filter(priority=2).order_by('?')
    paginator = Paginator(product_list, 8)
    products = paginator.get_page(page)
    return render(request, 'products.html', {
        'products': products,
        'current_collection': 'women'
    })

def accessories_products(request):
    page = request.GET.get('page', 1)
    product_list = Product.objects.filter(priority=3).order_by('?')
    paginator = Paginator(product_list, 8)
    products = paginator.get_page(page)
    return render(request, 'products.html', {
        'products': products,
        'current_collection': 'accessories'
    })