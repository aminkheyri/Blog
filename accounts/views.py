from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
from django.contrib.auth.models import User


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['user_name']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'congrats you have logged in to your account ', 'success')
                return redirect('blog:all_article')
            else:
                messages.error(request, 'Wrong username or password', 'danger')
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd['user_name'], cd['email'], cd['password1'])
            messages.success(request, 'Congrats You Registered successfully Now Please log in')
            return redirect('accounts:user_login')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html ', {'form': form})


def user_logout(request):
    logout(request)
    messages.success(request, 'You logged out successfully', 'success')
    return redirect('blog:all_article')