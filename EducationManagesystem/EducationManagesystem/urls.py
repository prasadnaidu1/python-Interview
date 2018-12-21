"""EducationManagesystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# from django.urls import path
from django.conf.urls import url
from harishApp import views

urlpatterns = [
    url('admin/', views.admin),
    url("index/",views.index),
    url("head/",views.head),
    url("menu/",views.menu),
    url("body/",views.body),
    url("course/",views.course),

    url("admin_login/",views.admin_login),
    url("login_validation/",views.admin_validation),
    url("admin_home/",views.admin_home),
    url("admin_menu/",views.admin_menu),
    url("admin_body/",views.admin_body),
    url("add_faculty/",views.add_faculty),
    url("add_student/",views.add_student),
    url("view_company/",views.view_company),
    url("admin_logout/",views.admin_Logout),

    url("course_details/",views.course_details),
    url("course_delete/",views.course_delete),
    url("course_update/",views.course_update),

    url("faculty_login/", views.faculty_login),
    url("faculty_details/", views.faculty_details),
    url("faculty_update/", views.faculty_update),
    url("faculty_delete/", views.faculty_delete),

    url("student_login/",views.student_login),
    url("student_details/",views.student_details),
    url("student_delete/",views.student_delete),

    url("company_registation/",views.company_registation),
    url("company_register/",views.company_register),
    url("company_approve/",views.company_approve),
    url("company_decline/",views.company_decline),
]
