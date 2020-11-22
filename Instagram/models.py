# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    profilephoto = models.ImageField(upload_to = 'imageprofile')
    Bio = models.CharField(max_length=30)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.Bio

        
    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()

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

class Comment(models.Model):
    comment = models.TextField()
    postt= models.ForeignKey(Image, on_delete=models.CASCADE)
    userr= models.ForeignKey(Profile, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, null=True)

class Follow(models.Model):
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='followers')

    def __str__(self):
        return f'{self.follower} Follow'    


     