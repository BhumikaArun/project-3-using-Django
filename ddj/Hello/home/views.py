from django.shortcuts import render,HttpResponse
from django.contrib import messages

from home.models import Contact
# Create your views here.
def index(request):
    context={
        "variable":"this is sent"
    }
    messages.success(request,"this is a test message")
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name, email=email, phone=phone,desc=desc)
        messages.success(request, "Your message has been sent!")
        contact.save()
    return render(request,'contact.html')