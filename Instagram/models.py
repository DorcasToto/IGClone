# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    profilephoto = models.ImageField(upload_to = 'images')
    Bio = models.CharField(max_length=30)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class Image(models.Model):
    image = models.ImageField(upload_to = 'images')
    imageName = models.CharField(max_length=30,blank=True)
    imageCaption = models.CharField(max_length=30)
    profile = models.ForeignKey(Profile,on_delete = models.CASCADE)
    likes = models.IntegerField(default=0,blank=True)
    comments = models.CharField(max_length=30,blank=True)

    def savePost(self):
        print(self)
        return self.save()


    def __str__(self):
        return self.imageName    

    
     