# import Http Response from django
from django.http import HttpResponse
from django.template.loader import render_to_string

# get datetime
import datetime

rendered = render_to_string('Add_course.html')