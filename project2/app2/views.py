from django.shortcuts import render
import datetime

# Create your views here.
def showindex(request):
    return render(request,"index.html")


def datedetails(request):
    id=request.POST.get("id")
    dob=request.POST.get("dob")
    doj=request.POST.get("doj")
    dobo=request.POST.get("dobo")
    from .models import impdates
    s1=impdates(id,dob,doj,dobo)
    print(s1)
    s1.save()
    return render(request,"index.html",{"msg":"data saved"})