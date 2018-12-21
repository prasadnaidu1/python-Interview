from django.db import models
class StockerLogin(models.Model):
    Name=models.CharField(max_length=30)
    Password=models.CharField(max_length=20)
class StockerRegister(models.Model):
    Name=models.CharField(max_length=40)
    Email=models.EmailField()
    Contact=models.IntegerField(default=10)
    Password=models.CharField(max_length=20)
