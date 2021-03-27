from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'default.html')

def login(request):
    if request.method == 'POST':
        uname = request.POST['userid']
        pwd = request.POST['pwd']
        user = auth.authenticate(username=uname, password=pwd)
        if user is not None:
            auth.login(request,user)
            return redirect("home")
        else:
            messages.info(request, "username or password is wrong")
            return redirect("login")
    else:
        return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        pwd = request.POST['pwd']
        uname = request.POST['userid']
        if User.objects.filter(email=email).exists():
            messages.info(request,"email already used")
            return redirect("login")
        elif User.objects.filter(username=uname).exists():
            messages.info(request,"username already used")
            return redirect("login") 
        else:
            user = User.objects.create_user(email=email, password=pwd, username=uname)
            user.save()
            return redirect("home")