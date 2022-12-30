from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.

def index(request):
    context ={
        "variable1":"Mahenga is great",
        "variable2":"Madhav is great"
    }
    return render(request,'index.html')
    # return HttpResponse('This Is Home Page')


def about(request):
    return render(request,'about.html')
    # return HttpResponse('This Is about Page')

def services(request):
    return render(request,'services.html')
    # return HttpResponse('This is Servcies page')

def contact(request):
    if request.method == 'POST':
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get('phone')
        desc=request.POST.get("desc")

        # creat model object end save data

        c1 = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        c1.save()
        messages.success(request, 'Your Form has been Submited!')
    return render(request,'contact.html')
    # return HttpResponse('This is contact page')

