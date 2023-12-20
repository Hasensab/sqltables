from django.shortcuts import render
from app.models import *
from django.db.models import Q

# Create your views here.
def display_dept(request):
    DTO=Dept.objects.all()
    DTO=Dept.objects.filter(DEPTNO=20)
    d={'dept':DTO}
    return render(request,'dept.html',d)
def display_emp(request):
    ETO=Emp.objects.all()
    ETO=Emp.objects.filter(DEPTNO=10,JOB='cricket')
    ETO=Emp.objects.filter(Q(DEPTNO=10) & Q(JOB='cricket'))
    ETO=Emp.objects.filter(Q(DEPTNO=10) | Q(JOB='cricket'))
    ETO=Emp.objects.filter(JOB='kabaddi',SAL__gte='50000')
    ETO=Emp.objects.filter(Q(JOB='kabaddi') & Q(SAL__gte='50000'))
    ETO=Emp.objects.filter(Q(JOB='kabaddi') | Q(SAL__gte='50000'))
    
    d={'emp':ETO}
    return render(request,'emp.html',context=d)

def display_author(request):
    ATO=Author.objects.all()
    d={'author':ATO}
    return render(request,'author.html',d)



