import re
from turtle import pos
from django.shortcuts import render, redirect, get_object_or_404
from sympy import content
from .models import Post, Comment
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

def home(request):
    
    posts = Post.objects.all()

    return render(request, 'blog/home.html',{
        'posts':posts
    })


def post_detail(request, id):
   
    post = get_object_or_404(Post, id=id)

    return render(request, 'blog/detail.html', {
        'post':post
    })


@login_required
def create_post(request):
    
    if request.method == "POST":
        
        title = request.POST.get("title")
        content = request.POST.get("content")

        Post.objects.create(
            title=title,
            content=content,
            author=request.user
        )
        
        return redirect('home')

    return render(request, 'blog/create.html')


@login_required
def edit_post(request, id):
    
    post = get_object_or_404(Post, id=id)
    if request.user != post.author:
        return redirect('home')

    if request.method == "POST":
        
        post.title = request.POST.get('title')
        
        post.content = request.POST.get('content')

        post.save()

        return redirect('detail', id=post.id)
    
    return render(request, 'blog/edit.html', {
        'post':post
    })


@login_required
def delete_post(request, id):
    
    post = get_object_or_404(Post, id=id)
    
    if request.user != post.author:
        return redirect('home')

    post.delete()

    return redirect('home')


def signup_view(request):
     
    if request.method == 'POST':

        form = UserCreationForm(request.POST)   

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect('home') 
    
    else:

        form = UserCreationForm()

    return render(request, 'blog/signup.html',{
        'form':form
    })


def login_view(request):

    if request.method == "POST":

        form = AuthenticationForm(data=request.POST)

        if form.is_valid():

            user = form.get_user()

            login(request, user)

            return redirect('home')
    
    else:

        form = AuthenticationForm()
    
    return render(request, 'blog/login.html', {
        'form':form
    })


def logout_view(request):
    
    logout(request)

    return redirect('home')



