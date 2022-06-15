from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')    

def profile(request):
    return render(request, 'profile.html')

def update_profile(request):
    return render(request, 'update_profile.html')   

def post(request):
    return render(request, 'post.html')     

def search(request):
    return render(request, 'search.html')

def ratings(request):
    return render(request, 'ratings.html')    
