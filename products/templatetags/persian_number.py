from django import template
from django.conf import settings
register = template.Library()

@register.filter
def to_persian(value):  

    if settings.LANGUAGE_CODE == 'fa':
        value=str(value)
        translation_table = value.maketrans('0123456789','۰۱۲۳۴۵۶۷۸۹')
        return value.translate(translation_table)
    else:
        return value