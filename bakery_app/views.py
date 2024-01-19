from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from django.http import HttpResponse
from django.template import loader
from .models import Product

def index (request):
    products = Product.objects.all()

    return render(request, 'index.html', {'products': products})

def menu (request):
    products = Product.objects.all()
    return render(request, 'menu.html', {'products': products})

def blog (request):
    template = loader.get_template('blog.html')
    blog = Product.objects.all().values()
    context = {
        'blog': blog,
    }
    return HttpResponse(template.render(context,request))

def contact (request):
    template = loader.get_template('contact.html')
    contact = Product.objects.all().values()
    context = {
        'contact': contact,
    }
    return HttpResponse(template.render(context,request))

def cart (request):
    template = loader.get_template('cart.html')
    cart = Product.objects.all().values()
    context = {
        'cart': cart,
    }
    return HttpResponse(template.render(context,request))

def checkout (request):
    template = loader.get_template('checkout.html')
    checkout = Product.objects.all().values()
    context = {
        'checkout': checkout,
    }
    return HttpResponse(template.render(context,request))

def productdetail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product_similar = Product.objects.filter(
        Q(name__icontains='cake') & ~Q(id=product.id)
    )[:4]
    return render(request, 'productdetail.html', {'product': product, 'product_similar': product_similar})
def about (request):
    temp = loader.get_template("about.html")
    product = Product.objects.all().values()
    context = {
        'product' :product,
    }
    return HttpResponse(temp.render(context,request))
