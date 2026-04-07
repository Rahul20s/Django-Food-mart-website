from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm
from .models import ProfileModel

def RegisterFunctionView(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')
        else:
            messages.error(request, 'Please fix the errors in the form.')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

def LoginFunctionView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('food:home')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'users/login.html')

def LogoutFunctionView(request):
    logout(request)
    return redirect('food:home')

def ProfileFunctionView(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'users/profile.html')