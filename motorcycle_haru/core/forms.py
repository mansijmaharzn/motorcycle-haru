from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter Username',
        'class': 'w-full p-3 rounded-xl'
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Enter Your Email',
        'class': 'w-full p-3 rounded-xl'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password',
        'class': 'w-full p-3 rounded-xl'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat Password',
        'class': 'w-full p-3 rounded-xl'
    }))


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter Username',
        'class': 'w-full p-3 rounded-xl'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password',
        'class': 'w-full p-3 rounded-xl'
    }))