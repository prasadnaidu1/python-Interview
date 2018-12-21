from django.shortcuts import render

# Create your views here.
def showindex(request):
    return render(request,"index.html")


def savedetails(request):
    id=request.POST.get("sno")
    name=request.POST.getlist("course")
    print(name)
    d1={"dates":name}
    from firebase import firebase as fab
    fa=fab.FirebaseApplication("https://student-5f369.firebaseio.com/",None)
    fa.put("impdates/",id,d1)


    return render(request,"index.html",{"msg":"saved data"})


def register(request):
    id=request.GET.get("update_id")
    print(id)
    if id==None:
        from firebase import firebase as fab
        fire=fab.FirebaseApplication("https://student-5f369.firebaseio.com/impdates",None)
        f1=fire.get("impdates/",None)
        return render(request,"show.html",{"res":f1})
    else:
        from firebase import firebase as fab
        fire = fab.FirebaseApplication("https://student-5f369.firebaseio.com/impdates", None)
        d1=fire.get("impdates/",id)
        return render(request,"index.html",{"key":id,"dates":d1["dates"]})

def deletedetails(request):
    id=request.POST.get("delete_id")
    print(id)
    from firebase import firebase as fab
    fa=fab.FirebaseApplication("https://student-5f369.firebaseio.com/impdates",None)
    f2=fa.delete("impdates/",id)
    print(f2)
    return register(request)
