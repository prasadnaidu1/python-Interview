from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import Serializer
from rest_framework import status
from .models import Emp
class EmpView(APIView):
    def get(self,request,format=None):
        emp=Emp.objects.all()
        serializer=Serializer(emp,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"New object is added to database"})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class Empdetails(APIView):
    def get(self,request,pk,format=None):
        emp=Emp.objects.get(empid=pk)
        serializer=Serializer(emp)
        return Response(serializer.data)
    def put(self,request,pk,format=None):
        emp=Emp.objects.get(empid=pk)
        serializer=Serializer(emp,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Object is Successfully updated"})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk,format=None):
        emp=Emp.objects.get(empid=pk)
        emp.delete()
        return Response({"message":"object is successfully Deleted"})
