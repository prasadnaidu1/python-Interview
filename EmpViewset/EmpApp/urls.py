from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from .views import EmpViewset
router=DefaultRouter
router.register("emp-viewset",EmpViewset,base_name="emp-viewset")
urlpatterns = [
    url(r"",include(router.urls))
]
