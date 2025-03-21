from django.db import models
from customers.models import Customer
from products.models  import Product

class Order(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICE=(
        (LIVE,'Live'),
        (DELETE,'Delete')
        )
    CART_STAGE=0
    ORDER_CONFORMED=1
    ORDER_PROCESSED=2
    ORDER_DELIVERED=3
    ORDER_REJECTED=4
    STATUS_CHOICE=((ORDER_CONFORMED,"ORDER_CONFORMED"),
                   (ORDER_DELIVERED,"ORDER_DELIVERED"),
                   (ORDER_REJECTED,"ORDER_REJECTED")
                   )
    order_status=models.IntegerField(choices=STATUS_CHOICE,default=CART_STAGE)
    
    owner=models.ForeignKey(Customer,on_delete=models.SET_NULL,related_name='order ')
    delete_status=models.IntegerField(choices=DELETE_CHOICE,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
class OrderedItem(models.Model):
    product=models.ForeignKey(Product,related_name="added_cart",on_delete=models.SET_NULL)
    quantity=models.IntegerField(default=1)
    owner=models.ForeignKey(Order,on_delete=models.CASCADEC,related_name='added_items')
    
    
    