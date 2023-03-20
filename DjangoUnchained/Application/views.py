from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def student_course(request):
    if request.method == "GET":
        return render(request, "courses_student.html")

def add_course(request):
    template = loader.get_template('Add_course.html')
    return HttpResponse(template.render())

# added to route admin.html in Application/templates
def admin_page(request):
    template = loader.get_template('admin.html')
    return HttpResponse(template.render())

