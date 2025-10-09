from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from .models import Feature

def index(request):
    objs = Feature.objects.all()
    return render(request, 'index.html', {'objs' : objs})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username = username, password = password1, email = email)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'passwords are not same')
            return redirect('register')
    else:
        return render(request, 'register.html')
    

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)  
        
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    
    else:
        return render(request, 'login.html')
    

def logout(request):
    auth.logout(request)
    return redirect('/')

def post(request, pk):
    return render(request, 'post.html', {'pk':pk})

def posts_count(request):
    posts = ['post1', 'post2', 'post3']
    return render(request, 'posts_count.html', {'posts':posts})