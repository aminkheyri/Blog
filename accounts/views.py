from django.shortcuts import render
from .forms import UserLoginForm


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['user_name']
            password = form.cleaned_data['password']
            print(username)
            print(password)
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})
