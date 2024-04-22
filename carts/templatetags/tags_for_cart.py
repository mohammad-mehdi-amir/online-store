from django import template
from django.conf import settings
from products.models import Product
register = template.Library()

    
# SHIPING_PRICE=Shiping_price.objects.get().shiping_price


@register.filter
def get_obj(val):
    print(val,'<---------------------')
    return Product.objects.get(id=val)