from django.urls import path

from APP1 import views

urlpatterns = [
    path("demo",views.demo1,name="demo"),
    path("home",views.home,name="home")
]