from django.shortcuts import render
from ShibaApp.forms import ShibaUserForm, ShibaProfileForm
# from ShibaApp.models import ShibaUser
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request, 'ShibaApp/index.html')

@login_required
def special(request):
    # Remember to also set login url in settings.py!
    # LOGIN_URL = '/basic_app/user_login/'
    return HttpResponse("You are logged in. Nice!")

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))



def user_profile(request):
    return render(request, 'ShibaApp/profile.html')

def user_photos(request):
    return render(request, 'ShibaApp/photos.html')

def newuser_register(request):
    registered = False

    if request.method == 'POST':
        user_form = ShibaUserForm(data=request.POST)
        profile_form = ShibaProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                print('found it')
                # If yes, then grab it from the POST form reply
                profile.profile_pic = request.FILES['profile_pic']

            print(request.FILES)

            profile.save()
            registered = True

        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = ShibaUserForm()
        profile_form = ShibaProfileForm()



    return render(request, 'ShibaApp/register.html', {'ShibaUserForm':user_form,'ShibaProfileForm':profile_form, "Registered":registered})

def user_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('ShibaApp:user_profile'))
            else:
                my_dict = {'user':username}
                return render(request,'login_failed.html',context=my_dict)
        else:
            return HttpResponse("Invalid login details supplied.")
    else:

        return render(request, 'ShibaApp/login.html')

def user_friends(request):
    return render(request, 'ShibaApp/friends.html')
