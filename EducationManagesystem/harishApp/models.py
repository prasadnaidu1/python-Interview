from django.db import models

class Course(models.Model):
    Id=models.IntegerField(default=2,primary_key=True)
    Name=models.CharField(max_length=123)
    Fee=models.DecimalField(max_digits=6,decimal_places=2)
    Duration=models.IntegerField(default=2)

class Faculty(models.Model):
    Id=models.IntegerField(default=3,primary_key=True)
    Name=models.CharField(max_length=123)
    Contact=models.IntegerField(default=10)
    Email=models.EmailField(max_length=90)
    Password=models.CharField(max_length=60)

class Student(models.Model):
    Id=models.IntegerField(default=4,primary_key=True)
    Name=models.CharField(max_length=123)
    Contact=models.IntegerField(default=10)
    Email=models.EmailField(max_length=90)
    Password=models.CharField(max_length=60)

class Company(models.Model):
    Id=models.IntegerField(default=5,primary_key=True)
    Name=models.CharField(max_length=40)
    HR_Name=models.CharField(max_length=50)
    Email=models.EmailField()
    Contact=models.IntegerField(default=10)
    Purpose=models.CharField(max_length=80)
    Address=models.CharField(max_length=342)
    Status=models.CharField(max_length=34)