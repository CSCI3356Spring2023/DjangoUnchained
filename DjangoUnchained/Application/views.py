from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from .forms import AddCourse
from .forms import StudentApply
from .forms import CourseAdd



from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def student_course(request):
    if request.method == "GET":
        return render(request, "courses_student.html")

def add_course(request):
    template = loader.get_template('Add_course.html')
    return HttpResponse(template.render())

# added to route admin.html in Application/templates
def admin_page(request):
    template = loader.get_template('admin_page.html')
    return HttpResponse(template.render())

def homepage(request):
    if request.user.is_authenticated:
        userRole = request.user.get_role()
        if (userRole == 'Student'):
            return render(request, "courses_student.html")
        elif (userRole == 'Instructor'):
            return render(request, "instructor_visual.html")
        elif (userRole == 'Administrator'):
            return render(request, "admin_page.html")
        else:
            return render(request, "homepage.html")
        
    else:
        return render("landingpage.html")

def student_apply(request):

    form = StudentApply()
    context = {}

    if request.method == 'POST':
        form = StudentApply(request.POST)
        if form.is_valid():
            form.save()
        
    context['form'] = form
    return render(request, "studentApply.html", context)

def temp_add_course(request):

    form = CourseAdd()
    context = {}

    if request.method == 'POST':
        form = CourseAdd(request.POST)
        if form.is_valid():
            form.save()
    print(form)
    context['form'] = form
    return render(request, "temp_add_course.html", context)

def Add_course(request):

    form = AddCourse()
    context = {}

    if request.method == 'POST':
        form = AddCourse(request.POST)
        if form.is_valid():
            form.save()
    print(form)
    context['form'] = form
    return render(request, "Add_course.html", context)
