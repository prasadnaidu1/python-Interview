from django.db import models

# Create your models here.
class impdates(models.Model):
    id=models.IntegerField(default=4,primary_key=True)
    dob=models.IntegerField(default=20)
    doj=models.IntegerField(default=20)
    bt=models.IntegerField(default=20)
