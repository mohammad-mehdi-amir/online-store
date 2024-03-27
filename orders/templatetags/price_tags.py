from django import template
from django.conf import settings
register = template.Library()

    
SHIPING_PRICE=45_000


@register.filter
def apply_shiping_price(total_price):
    return total_price+SHIPING_PRICE

@register.filter
def to_int(price):
    return int(price)