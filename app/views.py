from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
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

def insert_data(request):
    a = int(input('Enter data: '))
    d = {'a':a}
    return HttpResponse('<h1>{{a}}</h1>')

