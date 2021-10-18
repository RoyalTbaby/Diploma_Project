from django.shortcuts import render
from . models import *


def shop(request):
    products = Product.objects.all
    context = {'products': products}
    return render(request, 'store/shop.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []

    context = {'items': items}
    return render(request, 'store/cart.html', context)



def payment(request):
    context = {}
    return render(request, 'store/payment.html', context)


def about(request):
    context = {}
    return render(request, 'store/about.html', context)