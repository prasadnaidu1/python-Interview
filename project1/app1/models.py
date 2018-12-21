from django.db import models

class student(models.Model):
    id=models.IntegerField(default=5,primary_key=True)
    name=models.CharField(max_length=50)
    cno=models.IntegerField(default=10)
