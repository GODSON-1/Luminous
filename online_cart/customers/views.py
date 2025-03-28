from django.shortcuts import render

# Create your views here.
def show_account(request):
    return render(request,'account.html',{'hide_blog_and_contact':True,'show_reg_log':True})

def show_about(request):
    return render(request,'about.html',{'hide_blog_and_contact':True})