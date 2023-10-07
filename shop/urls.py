from django.urls import path
from .views import app,allproducts,store,cart,checkout

urlpatterns = [
                path('',app,name='app'),
                path('allproducts',allproducts,name ='allproducts'),
                path('store',store,name="store"),
                path('cart',cart,name="cart"),
                path('checkout',checkout,name="checkout")
            ]
