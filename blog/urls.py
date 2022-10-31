from unicodedata import name
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.views import View

from blog import views

from  .views import logout_view,profileView, LoginView ,dispalyTime,Greetme, Myview, post_detail, Book_list, Post_list, post_detail
from .models import Post
from django.conf.urls.static import static

app_name = 'blog'

urlpatterns = [
    path("post/",Post),
    path("book_list/",Book_list),
    # path("", Post_list),
    path("contact/",Greetme),
    path("About/", Myview.as_view(),name="About"),
    path("login/",LoginView, name='login'),
    
    # post views
    path("",Post_list,name="home"),
    path("profile/",profileView,name="profile"),
    path("logout/",logout_view,name="logout"),
    path("<int:year>/<int:month>/<int:day>/<slug:post>/",post_detail,name="post_detail"),
           
]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)