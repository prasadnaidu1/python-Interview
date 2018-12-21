from django.shortcuts import render
from .models import student


def showindex(request):
    res=student.objects.all()
    return render(request,"index.html",{"stu":res})
def savedetails(request):
    id=request.POST.get("id")
    name=request.POST.get("name")
    cno=request.POST.get("cno")
    s1=student(id=id,name=name,cno=cno)
    s1.save()
    d1={"msg":"data saved",}
    res = student.objects.all()
    return render(request,"index.html",{"stu":res})


def deletedetails(request):
    id=request.POST.get("delete_id")
    print(id)
    res1=student.objects.filter(id=id).delete()
    print(res1)
    res = student.objects.all()
    return render(request,"index.html",{"stu":res})


def updatedetails(request):
    u_id=request.GET.get("update_id")
    print(u_id)
    res2=student.objects.filter(id=u_id).values()
    res3=student.objects.filter(id=u_id).update()
    res = student.objects.all()
    return render(request,"index.html",{"no":u_id})