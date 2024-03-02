from django import template
from django.conf import settings
register = template.Library()

@register.filter
def custom_add(val1,val2):  
    
    return int(val1-(float(val1)*float(val2)))
    
@register.filter
def get_sec(val):

    try:
        return val[1].image.url
    except:
        return val.first().image.url