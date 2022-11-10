from unicodedata import name
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.views import View
from . import views
# from blog import views

from  blog.views import logout_view,profileView, LoginView ,dispalyTime,Greetme, Myview, post_detail, Book_list, Post_list, post_detail, Addpostview,Postlistview,EditPostView,DeletePost,UpdateView
from django.conf.urls.static import static

app_name = 'blog'

urlpatterns = [
    path("post/",post_detail),
    path("book_list/",Book_list),
    # path("", Post_list),
    path("contact/",Greetme),
    path("About/", Myview.as_view(),name="About"),
    path("login/",LoginView, name='login'),
    
    # post views

    
    path("",Post_list,name="home"),
    path("profile/",profileView,name="profile"),
    path("logout/",logout_view,name="logout"),
    path('post_list/',Postlistview.as_view(),name='post_list'),
    path("<int:year>/<int:month>/<int:day>/<slug:post>/",post_detail,name="post_detail"),
    path('add_post/',Addpostview.as_view(),name="add_post"),
    path("update_post/<int:pk>/",EditPostView.as_view(),name='update-post'),
    
    # deleting path
    path("<id>/delete",DeletePost,name='delete_post')
           
]
# if settings.DEBUG:
#     urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)