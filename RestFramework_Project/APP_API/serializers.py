from rest_framework import serializers
from .models import Emp
class Serializer(serializers.ModelSerializer):
    class Meta:
        model=Emp
        fields=("empid","empname","salary")