from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.
class ShibaUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    profile_bio = models.CharField(max_length=500)

    def __str__(self):
        return self.user.username
