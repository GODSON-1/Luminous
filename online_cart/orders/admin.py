from django.contrib import admin
from orders.models import Order,OrderedItem  # noqa: F401
# Register your models here.
admin.site.register(Order)