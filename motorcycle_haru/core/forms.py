from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core import validators


def password_validator(password):
    if len(password) < 8:
        raise forms.ValidationError('Password must be at least 8 characters long.')

    elif password.isdigit():
        raise forms.ValidationError('Password must contain at least one letter.')
    
    elif password.isalpha():
        raise forms.ValidationError('Password must contain at least one number.')

    elif password.islower():
        raise forms.ValidationError('Password must contain at least one uppercase letter.')
    
    elif password.isupper():
        raise forms.ValidationError('Password must contain at least one lowercase letter.')
    
    elif password.isalnum():
        raise forms.ValidationError('Password must contain at least one special character.')


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter Username',
        'class': 'w-full p-3 rounded-xl'
    }),
        validators = [validators.MaxLengthValidator(150)]
    )

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Enter Your Email',
        'class': 'w-full p-3 rounded-xl'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password',
        'class': 'w-full p-3 rounded-xl'
    }),
        validators = [password_validator]
    )

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