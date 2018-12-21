from django.db import models

class Emp(models.Model):
    empid=models.IntegerField(default=3,primary_key=True)
    empname=models.CharField(max_length=40)
    email=models.EmailField(max_length=40)
    contact=models.IntegerField(default=10)
    sal=models.DecimalField(max_digits=8,decimal_places=2)
