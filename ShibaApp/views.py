from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'ShibaApp/index.html')

def user_profile(request):
    return render(request, 'ShibaApp/profile.html')

def user_photos(request):
    return render(request, 'ShibaApp/photos.html')

def newuser_register(request):
    return render(request, 'ShibaApp/register.html')

def user_login(request):
    return render(request, 'ShibaApp/login.html')

def user_friends(request):
    return render(request, 'ShibaApp/friends.html')
