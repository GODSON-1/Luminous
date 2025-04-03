from django.shortcuts import render,redirect # noqa: F401
from .models import Order,OrderedItem # noqa: F401
from products.models import Product # noqa: F401
# Create your views here.
def add_to_cart(request):
    if request.POST:
        user=request.user
        customer=user.customer_profile # noqa: F841
        quantity=int(request.POST.get('quantity'))  # noqa: F841
        product_id=request.POST.get('product_id')# noqa: F841
        size=request.POST.get('size') # noqa: F841
        cart_obj,created=Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE
            
            )
        product=Product.objects.get(pk=product_id)
        ordered_item,created=OrderedItem.objects.get_or_create(# noqa: F841
            product=product,
            owner=cart_obj,
        )
        if created:
            ordered_item.quantity=quantity
            ordered_item.save()
        else:
            ordered_item.quantity=ordered_item.quantity+quantity
            ordered_item.save()
            
    return redirect('orders:cart')

def show_cart(request):
    user=request.user
    customer=user.customer_profile  # noqa: F841
    cart_obj,created=Order.objects.get_or_create(
        owner=customer,
        order_status=Order.CART_STAGE
    )
    context={'cart':cart_obj}  # noqa: F841
    return render(request,'cart.html',context)

def remove_item_from_cart(request,pk):
    item=OrderedItem.objects.get(pk=pk)  # noqa: F841
    if item:
        item.delete()
    return redirect('orders:cart')