from django.shortcuts import render,redirect

def contactSection(request):
    return render(request,'contactus.html')

def aboutSection(request):
    return render(request,'aboutus.html')

# Create your views here.
