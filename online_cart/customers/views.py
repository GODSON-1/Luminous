from django.shortcuts import render,redirect 
from django.contrib.auth.models import User  
from .models import Customer
from django.contrib.auth import authenticate,login,logout # noqa: F401
from django.contrib import messages  
# Create your views here.

def signout(request):
    logout(request)
    return redirect('home')

def show_account(request):
    context={'hide_blog_and_contact':True,
             'show_reg_log':True,}  # noqa: F841
    if request.POST and 'register' in  request.POST:
        context['register']=True
        try:
            username=request.POST.get('username') 
            email=request.POST.get('email') 
            phone=request.POST.get('phone') 
            address=request.POST.get('address') 
            password=request.POST.get('password')  
            #create user account    
            user=User.objects.create_user( 
                name=username,
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
            success_message="User successfully created" # noqa: F841
            messages.success(request,success_message)
            return redirect('home')
        except Exception as e:  # noqa: F841
            error_message="Dulipcate username or invalid input" # noqa: F841
            messages.error(request,error_message)       
    if request.POST and 'login' in  request.POST: 
            context['register']=False  
            username=request.POST.get('username') 
            password=request.POST.get('password')  
            user=authenticate(username=username,password=password)
            if user:
                login(request,user)
                return redirect('home')
            else:
                error_message="invalid Username/Password" # noqa: F841
                messages.error(request,error_message)
                
                
          
    return render(request,'account.html',context)

def show_about(request):
    return render(request,'about.html',{'hide_blog_and_contact':True})