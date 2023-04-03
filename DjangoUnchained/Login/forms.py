# authentication/forms.py
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from Login.models import CustomUser
from django import forms
from django.forms.widgets import PasswordInput, TextInput

class LoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'BC Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class SignupForm(UserCreationForm):
    role_choices = [
        ('default', "Select Role"),
        ('instructor', "Instructor"),
        ('student', "Student"),
        ('administrator', "Administrator")
    ]
    
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'BC Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    role = forms.CharField(widget=forms.Select(choices=role_choices))
    
    class Meta(UserCreationForm.Meta):
        User = get_user_model()
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'role',]
