import email
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .forms import CreateUserForm 
from django.views.generic import UpdateView
from django.urls import reverse_lazy


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


# this will handle edit functionality

class UserEddView(UpdateView):
    model = User
    form_class = UserChangeForm
    template_name = 'registration/editprofile.html'
    success_url = reverse_lazy('bolg:profile')