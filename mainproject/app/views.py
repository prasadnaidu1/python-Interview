from django.shortcuts import render
from .models import StockerLogin,StockerRegister
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"index.html")
def Employee(request):
    return render(request,"employee.html")
def Stocker(request):
    if request.method == "POST":
        name=request.POST['sname']
        password=request.POST['pwd']
        res=StockerLogin(Name=name,Password=password)
        return render(request,"index.html",{"data":res})
    else:
        return render(request,"stocker.html")
def stockerRegister(request):
    if request.method =="POST":
        Name=request.POST['srname']
        Email=request.POST['sremail']
        Contact=request.POST['srcontact']
        Password=request.POST['srpassword']
        res=StockerRegister(Name=Name,Email=Email,Contact=Contact,Password=Password)
        res.save()
        return HttpResponse("sucessfully Register You can Login Now")
    else:
        return render(request,"stockerregister.html")