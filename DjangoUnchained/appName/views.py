from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def landing_page(request):
    template = loader.get_template('landingpage.html')
    return HttpResponse(template.render())

def add_course(request):
    template = loader.get_template('Add_course.html')
    return HttpResponse(template.render())

def student_login(request):
    if request.method == "GET":
        return render(request, "student.html")
    
def instructor_login(request):
    if request.method == "GET":
        return render(request, "instructor.html")
    
def administrator_login(request):
    if request.method == "GET":
        return render(request, "admin.html")