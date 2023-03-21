from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.conf import settings

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
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, "registration/login.html", {'form': form})
    
    