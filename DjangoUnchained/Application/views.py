from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from .forms import StudentApply
from .forms import CourseAddForm

from .models import CourseAdd


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
    courseInfo = CourseAdd.objects.all()
    courses = {'Courses': courseInfo}
    return render(request, 'admin_page.html', courses)

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

    form = CourseAddForm()
    context = {}

    if request.method == 'POST':
        form = CourseAddForm(request.POST)
        if form.is_valid():
            form.save()
    
    context['form'] = form
    return render(request, "temp_add_course.html", context)

def course_list(request):

    #template = loader.get_template('course_list.html')

    courseInfo = CourseAdd.objects.all()

    courses = {'Courses': courseInfo}

    #return HttpResponse(template.render(courses, request))

    return render(request, 'course_list.html', courses)

