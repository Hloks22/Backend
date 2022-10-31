import email
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm 


# Create your views here.

def regiterview(request):
    form=CreateUserForm()
    if request.method=='POST':
        form= CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data['username']
            email = form.cleaned_data['email']
            password=form.cleaned_data['password1']
            user = authenticate(username=username, email=email, password=password)
            login(request, user)
            messages.success(request, 'Your account has been created')
            return redirect('blog:profile')
    else:
        form= CreateUserForm()    
    return render(request, "registration/signup.html", {"form":form})