from django.urls import path
from . import views #. means all

urlpatterns = [
    path('home',views.home, name="home"),   
    path('login',views.login,name="login"),
    path('register',views.register,name="register")
]