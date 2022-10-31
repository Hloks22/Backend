from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import  regiterview

from  .import views
app_name='account'

urlpatterns = [
   path("signup/",regiterview,name="signup"),
         
]
