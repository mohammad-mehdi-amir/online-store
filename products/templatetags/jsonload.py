# Create a template_tags.py file in one of your apps (e.g., myapp)
# Ensure that the __init__.py file is present in the same directory

from django import template
import json

register = template.Library()

@register.filter
def json_loads(value):
    print(json.loads(value),)
    return json.loads(value)