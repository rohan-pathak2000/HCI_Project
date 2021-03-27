from django.urls import path
from . import views #. means all

urlpatterns = [
    path('about',views.aboutSection, name="about"), 
    path ('contact',views.contactSection, name="contact") 
]