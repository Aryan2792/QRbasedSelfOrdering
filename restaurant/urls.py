from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('menu', menu, name='menu'),
    path('loginUser', loginUser.as_view(), name='loginUser'),
    path('checkUser', checkUser.as_view(), name='checkUser'),
    path('addToCart/<int:id>', addToCart.as_view(), name='addToCart'),
    path('getCartQuantity', getCartQuantity, name='getCartQuantity'),
    path('cart', cart, name='cart'),
    path('about', about, name='about'),
    path('userlogout', userlogout, name='userlogout'),
    path('orders', order, name='orders'),
    path('getCartDetails', getCartDetails, name='getCartDetails'),
    path('removeCart/<int:id>', removeCart, name='removeCart'),
    path('changeQuantity/<int:id>/<int:q>', changeQuantity, name='changeQuantity'),
    path('confirmOrder', confirmOrder.as_view(), name='confirmOrder'),
    path('thankspage/<int:id>', thankspage, name='thankspage'),
    path('orderdetails/<int:id>', orderdetails, name='orderdetails'),

]