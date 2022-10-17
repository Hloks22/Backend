from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime

def welcome(reqest):
    html = "Welcome to my Economist website"
    return HttpResponse(html)