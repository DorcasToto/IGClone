# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Image,Profile,Comment,Follow

from django.contrib import admin

# Register your models here.
admin.site.register(Image)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Follow)