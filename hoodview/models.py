from unicodedata import name
from django.db import models

# Create your models here.
#1.Neighbourhood class,2.User class,3.Profile class,Busiiness,Post

class Neighbourhood(models.Model):
    name = models.CharField(max_length=60)
    location = models.CharField(max_length=70)
    description = models.TextField(max_length=255,help_text="Description of the Neighbourhood.")
    health_tel = models.IntegerField(max_length=100,null=True,blank=True)
