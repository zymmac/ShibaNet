from django import forms
from ShibaApp.models import ShibaUser
from django.contrib.auth.models import User

class ShibaUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username','email','password']
        # widgets = {
        #     'profile_bio': Textarea(attrs={'cols': 80, 'rows': 20}),
        # }

class ShibaProfileForm(forms.ModelForm):
    class Meta:
        model = ShibaUser
        fields = ['profile_pic','profile_bio']
