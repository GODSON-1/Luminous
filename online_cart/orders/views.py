from django.shortcuts import render,redirect
from .models import Order,OrderedItem
from django.contrib import messages # noqa: F401
from products.models import Product 
from django.contrib.auth.decorators import login_required # noqa: F401
# Create your views here.
def checkout_cart(request):
        if request.POST:
            try:
                user=request.user
                customer=user.customer_profile # noqa: F841
                total=float(request.POST.get('total'))  # noqa: F841
                order_obj=Order.objects.get(# noqa: F841
                    owner=customer,
                    order_status=Order.CART_STAGE
                    
                )
                if order_obj:
                    order_obj.order_status=Order.ORDER_CONFORMED
                    order_obj.save()
                    status_message="Your order is processed . your item will be delivered with in two day "  # noqa: F841
                    messages.success(request,status_message)
                else:
                    status_message="Unable to process.No items in cart "  # noqa: F841
                    messages.error(request,status_message)
            except Exception as e:  # noqa: F841
                status_message="Unable to process.No items in cart "  # noqa: F841
                messages.error(request,status_message)       
    
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


@login_required(login_url='account')
def show_orders(request):
    user=request.user
    customer=user.customer_profile 
    all_orders=Order.objects.filter(owner=customer).exclude(order_status=Order.CART_STAGE)# noqa: F841
    context={'orders':all_orders } # noqa: F841
    return render(request,'orders.html',context)


@login_required(login_url='account') # type: ignore
def add_to_cart(request):
    if request.POST:
        user=request.user
        customer=user.customer_profile 
        quantity=int(request.POST.get('quantity'))  
        product_id=request.POST.get('product_id')
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
