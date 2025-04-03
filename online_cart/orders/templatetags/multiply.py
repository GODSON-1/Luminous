from django import template
from decimal import Decimal
register=template.Library()

@register.simple_tag(name='multiply')
def multiply(a,b):
    try:
        return Decimal(a) * int(b)
    except (ValueError, TypeError):
        return 0