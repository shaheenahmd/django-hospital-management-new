from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

from .models import Departments,Doctors

# Create your views here.
def index(request):
    # return  HttpResponse("home working")
    return render(request,"index.html")

def about(request):
    # return  HttpResponse("about working")
     return render(request,"about.html")
    
def contact(request):
    # return HttpResponse("contact working")
     return render(request,"contact.html")

def doctors(request):
    # return HttpResponse("doctors working")
    dict_doctors={
        'doctor':Doctors.objects.all()
    }
    return render(request,"doctors.html",dict_doctors)

def departments(request):
    # return HttpResponse("department is working")
    dict_departments={
        'dept':Departments.objects.all()
    }
    return render(request,"departments.html",dict_departments)

