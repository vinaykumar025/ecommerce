from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader

from .models import Product

def app(request):
    return render(request,'shop/loginn.html')

def allproducts(request):
    template = loader.get_template('shop/allproducts.html')
    context = {'allproducts': Product.objects.all()}
    return HttpResponse(template.render(context, request))
    ##products  = Product.objects.all()
    #context = {'products':products}
    #return HttpResponse(render(request,'shop/allproducts.html'))

# Create your views here.


def store(request):
    context = {}
    return render(request,'shop/store.html',context)

def cart(request):
    context = {}
    return render(request,'shop/cart.html',context)

def checkout(request):
    context = {}
    return render(request,'shop/checkout.html',context)