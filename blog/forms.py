from dataclasses import field
from xml.parsers.expat import model
from .models import Comment

from django import forms

class commentform(forms.ModelForm):
    
    class Meta:
        model= Comment
        fields=('name','email','body')