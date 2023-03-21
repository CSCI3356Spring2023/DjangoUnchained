from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def landing_page(request):
    template = loader.get_template('landingpage.html')
    return HttpResponse(template.render())

def student_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/website/profile/')
    else:
        form = AuthenticationForm()
    return render(request, "registration/login.html", {'form': form})
    
def instructor_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/website/profile/')
    else:
        form = AuthenticationForm()
    return render(request, "registration/login.html", {'form': form})
    
def administrator_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/website/profile/')
    else:
        form = AuthenticationForm()
    return render(request, "registration/login.html", {'form': form})
    