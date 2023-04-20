from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from .forms import StudentApply
from .forms import CourseAddForm
from django.shortcuts import get_object_or_404, redirect

from .models import CourseAdd
from .models import StudentApplication

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def student_course(request):
    if request.method == "GET":
        return render(request, "courses_student.html") 

def add_course(request):
    if request.user.is_authenticated:
        userRole = request.user.get_role()
        if (userRole == 'Instructor' or userRole == "Administrator"):
            return render(request,'Add_course.html')
        else:
            return render(request, '404.html')
    else:
        return render(request, '404.html')

# added to route admin.html in Application/templates
def admin_page(request):
    courseInfo = CourseAdd.objects.all()
    applicantInfo = StudentApplication.objects.all()
    context = {'Courses': courseInfo, 'Applicants': applicantInfo}

    return render(request, 'admin_page.html', context)

def homepage(request):
    if request.user.is_authenticated:
        userRole = request.user.get_role()
        if (userRole == 'Student'):
            return render(request, "courses_student.html")
        elif (userRole == 'Instructor'):
            return render(request, "instructor_visual.html")
        elif (userRole == 'Administrator'):
            return admin_page(request)
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

    #template = loader.get_template('course_list.html')]
    courseInfo = CourseAdd.objects.all()

    courses = {'Courses': courseInfo}

    print('courses: ', courses)

    #return HttpResponse(template.render(courses, request))

    return render(request, 'course_list.html', courses)

def delete_course(request, course_id):
    course = get_object_or_404(CourseAdd, id=course_id)
    course.delete()
    return redirect('admin_page')  # Redirect to the admin_page or the page where you display the list of courses


def delete_applicant(request, applicant_id):
    course = get_object_or_404(StudentApplication, id=applicant_id)
    course.delete()
    return redirect('admin_page')  # Redirect to the admin_page or the page where you display the list of courses

def application_list(request):

    #template = loader.get_template('application_list.html')
    name = request.user.get_name()
    courseAppliedTo = CourseAdd.objects.filter(CourseAdd.username==name)

    applications = {'Applications': courseAppliedTo}

    #return HttpResponse(template.render(courses, request))

    return render(request, 'application_list.html', applications)
