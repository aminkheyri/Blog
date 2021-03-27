from django import forms
from django.contrib.auth.models import User

class UserLoginForm(forms.Form):
    user_name = forms.CharField(max_length=30, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Your Username'}))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Your Password'}))


class UserRegistrationForm(forms.Form):
    user_name = forms.CharField(max_length=30, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Your Username'}))
    email = forms.EmailField(max_length=50, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Your Email'}))
    password1 = forms.CharField(label='password', max_length=50, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Your Password'}))
    password2 = forms.CharField(label='password conformation', max_length=50, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Confirm Your Password'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email)
        if user.exists():
            raise forms.ValidationError('The email is already exists')
        return email

    # def clean_password2(self):
    #     p1 = self.cleaned_data['password1']
    #     p2 = self.cleaned_data['password2']
    #     if p1 !=p2:
    #         raise forms.ValidationError("Your Passwords must match")

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data['password1']
        p2 = cleaned_data['password2']
        if p1 and p2:
            if p1 != p2:
                raise forms.ValidationError('Your Passwords must match')