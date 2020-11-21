from django.urls import include,path,re_path
from . import views

urlpatterns = [
    path('',views.index,name = 'home'),
    path('accounts/login',views.login,name = 'login')
]