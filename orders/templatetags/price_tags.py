from django import template
from django.conf import settings
from orders.models import Shiping_price
register = template.Library()

    
# SHIPING_PRICE=Shiping_price.objects.get().shiping_price
SHIPING_PRICE=45000


@register.filter
def apply_shiping_price(total_price):
    return total_price+SHIPING_PRICE

@register.filter
def to_int(price):
    return int(price)