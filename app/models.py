from django.db import models

# Create your models here.
class Dept(models.Model):
    DEPTNO=models.IntegerField(primary_key=True)
    DNAME=models.CharField(max_length=100,)
    LOC=models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.DNAME
    def __str__(self):
        return self.LOC


class Emp(models.Model):
    EMPNO=models.IntegerField(primary_key=True)
    ENAME=models.CharField(max_length=100)
    JOB=models.CharField(max_length=100)
    MGR=models.IntegerField()
    HIREDATE=models.DateField()
    SAL=models.PositiveIntegerField()
    COMM=models.FloatField()
    DEPTNO=models.ForeignKey(Dept,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.ENAME
    def __str__(self):
        return self.JOB
    
   
    
    
    

class Author(models.Model):
    Author_id=models.IntegerField(primary_key=True)
    Author_name=models.CharField(max_length=100,unique=True)
    
    def __str__(self):
        return self.Author_name
    

class Books(models.Model):
    Book_id=models.PositiveIntegerField(primary_key=True)
    Book_name=models.CharField(max_length=100)
    Book_price=models.PositiveIntegerField()
    Author_id=models.OneToOneField(Author,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Book_name
    
    
