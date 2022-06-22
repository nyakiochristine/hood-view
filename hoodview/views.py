from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .forms import BusinessForm,SignupForm,NeighbourhoodForm
from .models import Business,Post,Neighbourhood,Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})


def hoods(request):
    all_hoods= Neighbourhood.objects.all()
    return render(request,'all_hood.html')

def create_hood(request):
    if request.method=="Post"
    form = NeighbourHoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.admin = request.user.profile
            hood.save()
            return redirect('hood')
    else:
        form = NeighbourHoodForm()
    return render(request, 'newhood.html', {'form': form})


def profile(request):
    return render(request, 'profile.html')    