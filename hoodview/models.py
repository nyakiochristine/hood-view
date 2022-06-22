from django.db import models
from django.contrib.auth.urls import User

# Create your models here.
#1.Neighbourhood class,.Profile class,Busiiness,Post

class Neighbourhood(models.Model):
    name = models.CharField(max_length=60)
    location = models.CharField(max_length=70)
    description = models.TextField(max_length=255,help_text="Description of the Neighbourhood.")
    health_tel = models.IntegerField(max_length=100,null=True,blank=True)
    police_tel = models.IntegerField(max_length=100,null=True)
    
    
    
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=80, blank=True)
    bio = models.TextField(max_length=240, blank=True)
    profile_picture = models.ImageField(upload_to='images/', default='.png')
    location = models.CharField(max_length=50, blank=True, null=True)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.SET_NULL, null=True, related_name='members', blank=True)
