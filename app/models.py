from django.db import models

# Create your models here.
class Dept(models.Model):
    DEPTNO=models.IntegerField(primary_key=True)
    DNAME=models.CharField(max_length=100,)
    LOC=models.CharField(max_length=100,unique=True)


class Emp(models.Model):
    EMPNO=models.IntegerField(primary_key=True)
    ENAME=models.CharField(max_length=100)
    JOB=models.CharField(max_length=100)
    MGR=models.IntegerField()
    HIREDATE=models.DateField()
    SAL=models.PositiveIntegerField()
    COMM=models.FloatField()
    DEPTNO=models.ForeignKey(Dept,on_delete=models.CASCADE)

class Author(models.Model):
    Author_id=models.IntegerField(primary_key=True)
    Author_name=models.CharField(max_length=100,unique=True)

class Books(models.Model):
    Book_id=models.PositiveIntegerField(primary_key=True)
    Book_name=models.CharField(max_length=100)
    Book_price=models.PositiveIntegerField()
    Author_id=models.OneToOneField(Author,on_delete=models.CASCADE)
