"""ShibaNet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from ShibaApp import views

app_name = 'ShibaApp'

urlpatterns = [
    path('profile/', views.user_profile, name='user_profile'),
    path('photos/', views.user_photos, name='user_photos'),
    path('register/', views.newuser_register, name='newuser_register'),
    path('friends/', views.user_friends, name='user_friends'),
    path('login/',views.user_login,name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
]
