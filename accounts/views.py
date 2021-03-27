from django.shortcuts import render,redirect
from .forms import UserLoginForm
from django.contrib.auth import login, authenticate
from django.contrib import messages


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
