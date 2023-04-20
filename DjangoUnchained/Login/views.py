from django.conf import settings
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from django.core.mail import BadHeaderError, send_mail
from django.core import mail
from .models import SendEmail

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
    return bclogin(request)

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
    
def send_email(request):

    if request.method == 'POST':
        subject = request.POST['subject']
        body = request.POST['body']
        from_email = request.POST['from_email']
        to_email = request.POST['to_email']

        connection = mail.get_connection()
        connection.open()

        email = mail.EmailMessage(subject, body, from_email, [to_email], connection=connection, fail_silently=False)
        email.send()

        connection.close()

    return render(request, "send_email.html", {})