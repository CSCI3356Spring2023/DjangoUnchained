from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def add_course(request):
    template = loader.get_template('Add_course.html')
    return HttpResponse(template.render())
