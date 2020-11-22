from django.urls import include,path,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name = 'home'),
    path('new/post/', views.newPost, name='newPost'),
    path('post/<id>', views.comment, name='comment'),
    path('profile/', views.profile, name='profile'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)