from dataclasses import field
from pyexpat import model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#create class user dased user forms

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username', 'password1', 'password2','email',]