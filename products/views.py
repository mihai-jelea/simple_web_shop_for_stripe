# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from shopping_cart.models import Order
from .models import Product


def product_list(request):
    # initialize products list
    object_list = Product.objects.all()
    # flag to know when to show the Go to Cart button
    product_in_cart = False
    # empty last order
    if Order.objects.first() and product_in_cart == False:
        product_in_cart = True

    context = {
        'object_list': object_list,
        'product_in_cart': product_in_cart
    }

    return render(request, "products/product_list.html", context)