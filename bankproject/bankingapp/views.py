from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User



# Create your views here.
def index(request):
    return render(request,"home.html")

def signup(request):
    if request.method=="POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1=request.POST.get('password1')
        password2 = request.POST.get('password2')

        # myuser = User.objects.create_user(username,email,password1)
        # myuser.save()

        messages.success(request, "Your Account has been successfully created.")
        return redirect('/signin')


    return render(request,'signup.html')

def signin(request):
    if request.method == 'POST':
        username= request.POST['username']
        password = request.POST['password']

        user= authenticate(username=username,password= password)
        if user is not None:
            login(request,user)
            username=user.username
            return render(request,"home.html",{'username:username'})
        else:
            messages.error(request,"False Credentials")
            return redirect('/registration')

    return render(request,'signin.html')

def registration(request):
    if request.method == "POST":
        return redirect('/forms')

    return render(request,"registration.html")

def forms(request):
    if request.method == 'POST':

        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['phone']

        myuser = User.objects.create_user(firstname,lastname, email)
        myuser.save()

        messages.success(request, "Your Application is submitted.")
        return redirect('/forms')

        # if User.objects.filter(email=email).exists():
        #     messages.info(request,'email already taken')
        # else:
        #     user= User.objects.create_user(username=username,firstname=firstname,lastname=lastname, email=email, phone=phone)
        #     user.save();

    return render(request,"forms.html")

def logout(request):
    pass