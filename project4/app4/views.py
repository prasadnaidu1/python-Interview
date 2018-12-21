from django.shortcuts import render

# Create your views here.
def showindex(request):
    return render(request,"index.html")


def registerdetails(request):
    name=request.POST.getlist("course")
    return render(request,"index.html",{"res":name})



