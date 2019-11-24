from django.conf.urls import url

from .views import (
    add_to_cart,
    empty_cart,
    get_current_order,
    checkout,
)

app_name = 'shopping_cart'

urlpatterns = [
    url(r'^add-to-cart/(?P<item_id>[-\w]+)/$', add_to_cart, name="add_to_cart"),
    url(r'^empty-cart/$', empty_cart, name="empty_cart"),
    url(r'^order-summary/$', get_current_order, name="order_summary"),
    url(r'^checkout/$', checkout, name='checkout'),
]