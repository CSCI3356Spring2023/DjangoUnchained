from django.shortcuts import render

# Create your views here.
from django.template.loader import render_to_string
rendered = render_to_string('Add_course.html')