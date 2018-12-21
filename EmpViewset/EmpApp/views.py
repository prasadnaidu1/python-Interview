from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Emp
from .serializers import EmpSerializer
class EmpViewset(viewsets.ViewSet):
    def list(self,request):
        res=Emp.objects.all()
        serializer=EmpSerializer(data=request.data)
        return Response("serializer Data is Save")
    def insert(self,request):
        serializer=EmpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":"new object added DB"})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def retrieve(self,request ,pk=None):
        res=Emp.objects.get(empid=pk)
        serial=EmpSerializer(res)
        return Response(serial.data)
    def updata(self,request,pk=None):
        res=Emp.objects.get(empid=pk)
        serial=EmpSerializer(res,data=request.data)
        if serial.is_valid():
            serial.save()
            return Response({"data":"updated sucessfully"})
        else:
            return Response(serial.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk=None):
        res=Emp.objects.get(empid=pk)
        res.delete()
        return Response({"data":"Deleted Sucessfull"})

