from django.conf import settings
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader

from . import forms


def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect("/")
    return render(request, 'registration/signup.html', context={'form': form})
# Create your views here.

def landing_page(request):
    if request.user.is_authenticated:
        current_user = request.user
        return redirect("main/")
    template = loader.get_template('landingpage.html')
    return HttpResponse(template.render())

def bclogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
        else: 
             form = forms.LoginForm(request.POST)
             #Need to add in an error here
    else:
        form = forms.LoginForm(request.POST)
    return render(request, "registration/login.html", {'form': form})
    
    