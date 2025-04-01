from django.shortcuts import render,redirect # noqa: F401
from django.contrib.auth.models import User  # noqa: F401
from .models import Customer  # noqa: F401
from django.contrib import messages  # noqa: F401
# Create your views here.
def show_account(request):
    if request.POST and 'register' in  request.POST:
        try:
            username=request.POST.get('username') # noqa: F841
            email=request.POST.get('email') # noqa: F841
            phone=request.POST.get('phone') # noqa: F841
            address=request.POST.get('address') # noqa: F841
            password=request.POST.get('password')  # noqa: F841
            #create user account    
            user=User.objects.create_user( # noqa: F841
                username=username,
                password=password,
                email=email
                )  
            #customer user account
            customer=Customer.objects.create(  # noqa: F841
                user=user,
                phone=phone,
                address=address,
            )
            return redirect('home')
        except Exception as e:  # noqa: F841
            error_message="Dulipcate username or invalid credentionals" # noqa: F841
            messages.error(request,error_message)

            
    return render(request,'account.html',{'hide_blog_and_contact':True,'show_reg_log':True})

def show_about(request):
    return render(request,'about.html',{'hide_blog_and_contact':True})