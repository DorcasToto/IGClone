# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    profilephoto = models.ImageField(upload_to = 'images')
    Bio = models.CharField(max_length=30)

class Image(models.Model):
    image = models.ImageField(upload_to = 'images')
    imageName = models.CharField(max_length=30)
    imageCaption = models.CharField(max_length=30)
    profile = models.ForeignKey(Profile,on_delete = models.CASCADE)
    likes = models.IntegerField()
    comments = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='', null=True ,related_name='author')

    
     