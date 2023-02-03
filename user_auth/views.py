from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
# from polls.views import *

# Create your views here.
def user_login(request):
    return render(request, 'authentication/login.html')

def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        messages.error(request, 'Bad Credentials!')
        return HttpResponseRedirect(
            reverse('user_auth:user_login')
        )
    else:
        login(request, user)
        return HttpResponseRedirect(
            reverse('user_auth:home')
        )

def home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(
            reverse('user_auth:user_login')
        )
    return render(request, 'polls/poll.html', {
        "username": request.user.username,
        "password": request.user.password
    })

def register(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exists! Choose another username")
            return render(request, 'authentication/register.html')

        if password1 != password2:
            messages.error(request, "Passwords do not match. Enter password again.")
            return render(request, 'authentication/register.html')

        user = User.objects.create_user(username=username, first_name=firstname, password=password1)
        user.set_password(password1)
        user.save()

        messages.success(request, "Your account has been created successfully!")
        return HttpResponseRedirect(
            reverse('user_auth:user_login')
        )

    return render(request, 'authentication/register.html')