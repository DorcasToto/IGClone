from django.urls import include,path,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name = 'home'),
    path('new/post/', views.newPost, name='newPost'),
    path('comment/<id>', views.comment, name='comment'),
    path('profile/', views.profile, name='profile'),
    path('prof/<username>', views.prof, name='prof'),
    path('edit_profile/', views.editProfile,name = 'update_profile'),
    path('search/', views.searchprofile, name='search'),
    path('follow/<id>', views.follow, name='follow'),
    path('like', views.likePost, name='like_post'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)