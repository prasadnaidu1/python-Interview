from django.shortcuts import render

# Create your views here.
from harishApp.models import *


def index(request):
    return render(request,"index.html")
def head(request):
    return render(request,"head.html")
def menu(request):
    return render(request,"menu.html")
def body(request):
    return render(request,"body.html")
def faculty_login(request):
    if request.method=="POST":
        useridno=request.POST["f_useridno"]
        password=request.POST["f_password"]
        res=Faculty.objects.filter(Id=useridno,Password=password)
        if not res:
            return render(request,"faculty_login.html",{"status":"Invalid Login"})
        else:
            return render(request,"faculty_home.html")
    else:
        return render(request, "faculty_login.html")
def admin(request):
    return render(request,"admin.html")
def admin_login(request):
    return render(request,"admin_login.html")
def admin_validation(request):
    if request.method == "POST":
        name=request.POST["admin_name"]
        password=request.POST["admin_password"]
        print(name,password)
        if name == "admin" and password == "admin":
            return render(request,"admin_menu.html")
        else:
            return render(request,"admin_login.html",{"data":"Invalid User"})
    else:
        return render(request,"admin_login.html")
def admin_home(request):
    return render(request,"admin_home.html")
def admin_menu(request):
    return render(request,"admin_menu.html")

def course_details(request):
    if request.method =="POST":
        id=request.POST["course_id"]
        name=request.POST["course_name"]
        fees=request.POST["course_fees"]
        duration=request.POST["course_duration"]
        A=Course(Id=id,Name=name,Fee=fees,Duration=duration)
        A.save()
        res1=Course.objects.all()
        res2=Course.objects.none()
        return render(request, "admin_body.html",{"one":{"data":res1},"two":{"data":res2}})
    else:
        res1 = Course.objects.all()
        res2 = Course.objects.none()
        return render(request, "admin_body.html", {"one": {"data": res1}, "two": {"data": res2}})
def course_delete(request):
    if request.method=="POST":
        id = request.POST["course_delete_id"]
        Course.objects.filter(Id=id).delete()
        res1 = Course.objects.all()
        res2 = Course.objects.none()
        return render(request, "admin_body.html", {"one": {"data": res1}, "two": {"data": res2}})
    else:
        res1 = Course.objects.all()
        res2 = Course.objects.none()
        return render(request, "admin_body.html", {"one": {"data": res1}, "two": {"data": res2}})
def course_update(request):
    if request.method=="POST":
        id = request.POST["course_update_id"]
        res2=Course.objects.filter(Id=id)
        res1 = Course.objects.all()
        return render(request, "admin_body.html", {"one": {"data": res1}, "two": {"data": res2}})
def admin_body(request):
    res1 = Course.objects.all()
    res2 = Course.objects.none()
    return render(request, "admin_body.html",{"one": {"data": res1}, "two": {"data": res2}})

def add_faculty(request):
    res1 = Faculty.objects.all()
    res2 = Faculty.objects.none()
    return render(request, "add_faculty.html", {"one": {"data": res1}, "two": {"data": res2}})
def faculty_details(request):
    if request.method == "POST":
        id = request.POST["faculty_id"]
        name = request.POST["faculty_name"]
        contact = request.POST["faculty_contact"]
        email = request.POST["faculty_email"]
        password = request.POST["faculty_password"]
        A = Faculty(Id=id, Name=name,Contact=contact,Email=email,Password=password)
        A.save()
        res1 = Faculty.objects.all()
        res2 = Faculty.objects.none()
        return render(request, "add_faculty.html", {"one": {"data": res1}, "two": {"data": res2}})
    else:
        res1 = Faculty.objects.all()
        res2 = Faculty.objects.none()
        return render(request, "add_faculty.html", {"one": {"data": res1}, "two": {"data": res2}})
def faculty_delete(request):
    if request.method=="POST":
        id = request.POST["faculty_delete_id"]
        Faculty.objects.filter(Id=id).delete()
        res1 = Faculty.objects.all()
        res2 = Faculty.objects.none()
        return render(request, "add_faculty.html", {"one": {"data": res1}, "two": {"data": res2}})
    else:
        res1 = Faculty.objects.all()
        res2 = Faculty.objects.none()
        return render(request, "add_faculty.html", {"one": {"data": res1}, "two": {"data": res2}})
def faculty_update(request):
    if request.method=="POST":
        id = request.POST["faculty_update_id"]
        res2=Faculty.objects.filter(Id=id)
        res1 = Faculty.objects.all()
        return render(request, "add_faculty.html", {"one": {"data": res1}, "two": {"data": res2}})

def add_student(request):
    res1=Student.objects.all()
    res2=Student.objects.none()
    return render(request, "add_student.html", {"one": {"data": res1}, "two": {"data": res2}})
def student_details(request):
    if request.method == "POST":
        id = request.POST["student_id"]
        name = request.POST["student_name"]
        contact = request.POST["student_contact"]
        email = request.POST["student_email"]
        password = request.POST["student_password"]
        A =Student(Id=id, Name=name,Contact=contact,Email=email,Password=password)
        A.save()
        res1 = Student.objects.all()
        res2 = Student.objects.none()
        return render(request, "add_student.html", {"one": {"data": res1}, "two": {"data": res2}})
    else:
        res1 = Student.objects.all()
        res2 = Student.objects.none()
        return render(request, "add_student.html", {"one": {"data": res1}, "two": {"data": res2}})
def student_delete(request):
    if request.method=="POST":
        id = request.POST["student_delete_id"]
        Student.objects.filter(Id=id).delete()
        res1 = Student.objects.all()
        res2 = Student.objects.none()
        return render(request, "add_student.html", {"one": {"data": res1}, "two": {"data": res2}})
    else:
        res1 = Student.objects.all()
        res2 = Student.objects.none()
        return render(request, "add_faculty.html", {"one": {"data": res1}, "two": {"data": res2}})

def view_company(request):
    res=Company.objects.all()
    return render(request, "view_company.html",{"data":res})
def company_register(request):
    return render(request,"company_registation.html",{"status":""})

def company_registation(request):
    id=request.POST["c_idno"]
    name=request.POST["c_name"]
    hr_name=request.POST["c_hr_name"]
    email=request.POST["c_email"]
    contact=request.POST["c_contact"]
    purpose=request.POST["c_purpose"]
    address=request.POST["c_address"]
    Status="pending"
    qwe=Company(Id=id,Name=name,HR_Name=hr_name,Email=email,Contact=contact,Address=address,Status=Status)
    qwe.save()
    return render(request,"company_registation.html",{"status":"Registation Sucessfull Done =====>Approval is Pending"})
def company_approve(request):
    id=request.GET["c_id"]
    status="approve"
    Company.objects.filter(Id=id).update(Status=status)
    res=Company.objects.all()
    return render(request,"view_company.html",{"data":res})
def company_decline(request):
    id = request.GET["c_id"]
    status = "decline"
    Company.objects.filter(Id=id).update(Status=status)
    res = Company.objects.all()
    return render(request, "view_company.html", {"data": res})


def admin_Logout(request):
    return render(request,"admin_logout.html")


def student_login(request):
    if request.method=="POST":
        S_ID=request.POST["student_login_id"]
        S_pass=request.POST["student_login_password"]
        res=Student.objects.filter(Id=S_ID,Password=S_pass)
        if not res:
            return render(request,"studentlogin.html",{"status":"Invalid  Student_ID and Password"})

        else:
            return render(request, "student_homepage.html")
    else:
        return render(request,"studentlogin.html")

def course(request):
    return render(request,"course.html")
