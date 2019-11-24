from django.conf import settings
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404

from products.models import Product

from shopping_cart.extras import generate_order_id
from shopping_cart.models import OrderItem, Order

import datetime
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


def add_to_cart(request, **kwargs):
    # filter products by id
    product = Product.objects.filter(id=kwargs.get('item_id', "")).first()
    # create orderItem of the selected product
    order_item, status = OrderItem.objects.get_or_create(product=product)
    # create new order
    user_order = Order.objects.create()
    # add item to order
    user_order.items.add(order_item)
    # show confirmation message
    messages.info(request, "Item was added to cart. You can proceed to checkout!")
    # refresh page
    return redirect(reverse('products:product-list'))


def empty_cart(request):
    # delete all orders
    Order.objects.all().delete()
    # refresh page
    return redirect(reverse('products:product-list'))


def get_current_order(request, **kwargs):
    # get current order (assuming that there can be only one at a given time)
    existing_order = Order.objects.first()

    context = {
        'order': existing_order
    }
    return render(request, 'shopping_cart/order_summary.html', context)



def checkout(request):
    # get current order (assuming that there can be only one at a given time)
    existing_order = Order.objects.first()
    # get Stripe public key
    publishKey = settings.STRIPE_PUBLISHABLE_KEY
    if request.method == 'POST':
        try:
            # get the stripe token passed from the form
            token = request.POST['stripeToken']

            # create stripe charge
            charge = stripe.Charge.create(
                # transform in the smallest unit - cents
                amount=100*existing_order.get_cart_total(),
                currency='usd',
                description='Example charge',
                source=token,
            )

            # display confirmation and charge id
            messages.success(request, "Payment was successful. Stripe Charge ID = " + charge.id)

        except stripe.CardError as e:
            # display error message if the card was declined
            messages.error(request, "Your card has been declined.")
            
    context = {
        'order': existing_order,
        'STRIPE_PUBLISHABLE_KEY': publishKey
    }

    return render(request, 'shopping_cart/checkout.html', context)

