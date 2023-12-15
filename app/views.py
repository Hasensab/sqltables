from django.shortcuts import render
from app.models import *

# Create your views here.
def display_dept(request):
    DTO=Dept.objects.all()
    d={'dept':DTO}
    return render(request,'dept.html',d)
def display_emp(request):
    ETO=Emp.objects.all()
    d={'emp':ETO}
    return render(request,'emp.html',context=d)

def display_author(request):
    ATO=Author.objects.all()
    d={'author':ATO}
    return render(request,'author.html',d)

