from __future__ import unicode_literals

from django.db import models

from products.models import Product


class OrderItem(models.Model):
    # an order item contains one product
    product = models.OneToOneField(Product, on_delete=models.SET_NULL, null=True)

    # get product name
    def __str__(self):
        return self.product.name


class Order(models.Model):
    # a collection of products (Order Items)
    items = models.ManyToManyField(OrderItem)

    # return all products in the order
    def get_cart_items(self):
        return self.items.all()

    # return 
    def get_cart_total(self):
        return sum([item.product.price for item in self.items.all()])

