# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import NewPostForm
from .models import Image, Profile

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    posts = Image.objects.all()
    # profile = Profile.objects.filter(user=Image.profile.id).first()
    # print('posts',posts)
    return render(request,'index.html',{"posts":posts})

@login_required(login_url='/accounts/login/')
def newPost(request):
    current_user = request.user
    user_profile = Profile.objects.get(user = current_user)
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)        
        if form.is_valid():
            image=form.cleaned_data.get('image')
            imageCaption=form.cleaned_data.get('imageCaption')
            post = Image(image = image,imageCaption= imageCaption, profile=user_profile)
            post.savePost()
        else:
            print(form.errors)

        return redirect('home')

    else:
        form = NewPostForm()
    return render(request, 'newPost.html', {"form": form})
     
def profile(request):
    pass