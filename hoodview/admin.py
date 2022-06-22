from re import A
from django.contrib import admin
from .models import Profile,Post,Business,Neighbourhood


admin.site.register(Profile)
admin.site.register(Business)
admin.site.register(Neighbourhood)
admin.site.register(Post)

# Register your models here.
