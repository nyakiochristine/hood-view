from distutils.command.upload import upload
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField

from django.contrib.auth.models import User
#from cloudinary import CloudinaryImage
# Create your models here.
#1.Neighbourhood class,.Profile class,Busiiness,Post

class Neighbourhood(models.Model):
    name = models.CharField(max_length=60)
    location = models.CharField(max_length=70)
    admin = models.CharField(max_length=30)
    description = models.TextField(max_length=255,help_text="Description of the Neighbourhood.")
    health_tel = models.IntegerField(null=True,blank=True)
    police_tel = models.IntegerField(null=True,blank=True)
    
    def __str__(self):
        return f'{self.name} hood'

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()
        
    @classmethod
    def find_neighborhood(cls, neighborhood_id):
        return cls.objects.filter(id=neighborhood_id)



    
    
    
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=80, blank=True)
    bio = models.TextField(max_length=240, blank=True)
    profile_picture = models.ImageField(upload_to='images/', default='default.png')
    location = models.CharField(max_length=50, blank=True, null=True)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.SET_NULL, null=True, related_name='members', blank=True)
    
    def __str__(self):
        return f'{self.user.username} profile'
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
    
    
class Business(models.Model):
    name = models.CharField(max_length=80, blank=True, null=True)
    email = models.EmailField(max_length=80, blank=True, null=True)
    description = models.TextField(blank=True)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, related_name='business')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='owner')
    
    def __str__(self):
            return f'{self.name} Business'

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def search_business(cls, name):
        return cls.objects.filter(name__icontains=name).all()

class Post(models.Model):
    title = models.CharField(max_length=80, blank=True, null=True)
    post = models.TextField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='post_owner')
    hood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, related_name='hood_post')
    