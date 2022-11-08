from cgitb import html
from unicodedata import name
from multiprocessing import context
from django.shortcuts import get_object_or_404, redirect
# Create your views here.
from django.http import HttpResponse
import datetime
from django.views.generic import  TemplateView
# from requests import post
from .models import Book, Post
from  .forms import commentform
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.  


def dispalyTime(reqest):
    now = datetime.datetime.now()
    html = "Time is {}" .format(now)
    return HttpResponse(html)


def Greetme(reqest):
    # html = "wlcome to my contact page"
    return render(reqest, "contacts.html")

# class based views
class Myview(TemplateView):
    template_name="index.html"
    # def get_context_data(self, **kwargs):
        
    #     context=super().get_context_data(**kwargs)
    #     template_name="index.html"
    #     context={
    #     'page':template_name
    #     }
        # return context 

def Book_list(request):
    books=Book.objects.all()
    return render(request, "Book_list.html",{"books":books})

def book_details(request,id):
    context = {
         "detail":get_object_or_404(Book, pk=id)
    }
    return render(request,"detail.html",context)



def Post_list(request):
    object_list = Post.objects.all()
    paginator = Paginator(object_list,3)
    page = request.GET.get("page")
    try:
        posts=paginator.page(page)
        
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, "index.html",{"posts":posts})


# view for single post 
def post_detail(request, year, month,day, post):
    post = get_object_or_404(Post, slug=post, status="published",publish__year=year, publish__month=month, publish__day=day)
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method=='Post':
        comment_form =commentform(data=request.Post)
        if comment_form.is_valid():
            new_comment=comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else: 
        comment_form =commentform()
    return render(request, "post_detail.html", {"post":post,"comments":comments,"comment_form":comment_form,'new_comment':new_comment})

def LoginView(request):
    if request.method== 'POST':
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"you are now logged in as {username}"),
                return redirect('blog:profile')
            else:
                messages.error(request, f"username/password is invalid")
        else:
                messages.error(request, f"username/password is invalid") 
    form=AuthenticationForm()  
    return render(request,"authenticate/login.html", context={"form":form})


@login_required(login_url='blog:login')
def profileView(request):
    return render(request, "profile.html")

def logout_view(request):
    logout(request)
    return redirect('/')