from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .forms import BusinessForm, PostForm,SignupForm,NeighbourhoodForm
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
    if request.method=="POST":
        
        form = NeighbourhoodForm(request.POST, request.FILES)
        
        if form.is_valid():
            hood = form.save(commit=False)
            hood.admin = request.user.profile
            hood.save()
            return redirect('hood')
    else:
        form = NeighbourhoodForm()
    return render(request, 'new_hood.html', {'form': form})


    



def profile(request):
    return render(request, 'profile.html')    

def edit_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile', user.username)
    else:
        form = UpdateProfileForm(instance=request.user.profile)
    return render(request, 'prof-edit.html', {'form': form})


def create_post(request, hood_id):
    
    hood = Neighbourhood.objects.get(id=hood_id)
    
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.hood = hood
            post.user = request.user.profile
            post.save()
            return redirect('single-hood', hood.id)
    else:
        form = PostForm()
    return render(request, 'post.html', {'form': form})


def search_business(request):
    if request.method == 'GET':
        name = request.GET.get('title')
        results= Business.objects.filter(name=name)
        
        
        print(results)
        params = {
            'results': results,
            'message': message,
        }
        return render(request, 'search_results.html', params)
    else:
        message = "You haven't searched for any image category"
    return render(request, "search_results.html")

