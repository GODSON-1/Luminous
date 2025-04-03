from django import template
from decimal import Decimal  # noqa: F401

register=template.Library()

@register.simple_tag(name='gettotal')
def gettotal(cart):
    total=0
    for item in cart.added_items.all():
        total += Decimal(str(item.product.price)) * item.quantity  # noqa: F821, F841
    return total
