from django.shortcuts import render
from django.contrib.auth.models import User,auth
# Create your views here.
def home(request):
    name = "Rohan"
    address = "GB Pant"
    phone = 69
    return render(request,'index.html',{'name':name,'addr':address,'phno':phone})

def register(request):
    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        username = request.POST['username']
        password = request.POST['pass']
        email = request.POST['email']
        user = User.objects.create_user(username=username,last_name = last_name, email=email, password=password)
        user.save()
        return render(request,'index.html',{'name': first_name, 'addr': email, 'phno':username})
    else:
        return render(request,'register.html')