from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name=""),
    path('user-dashboard',views.userdashboard,name="user-dashboard"),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
]