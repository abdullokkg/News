from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate,login
# Create your views here.
def login_view(request):
    if request.method == "POST":
        form =  LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return redirect("home")
            else:
                messages.add_message(request,messages.ERROR,"user not found")
        else: 
            messages.add_message(request,messages.ERROR,"user not found")
            return render(request,'login.html')
    return render(request,'login.html')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            messages.add_message(request,level=messages.ERROR,message=form.errors)
            return render(request,'register.html')
    return render(request,'register.html')