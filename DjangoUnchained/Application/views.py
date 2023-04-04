from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

from .forms import AddCourse, StudentApply
from .models import AddCourse, StudentApplication
from .forms import AddCourseForm, StudentApplicationForm


# Create your views here.

def student_course(request):
    if request.method == "GET":
        return render(request, "courses_student.html")

def add_course(request):
    template = loader.get_template('Add_course.html')
    return HttpResponse(template.render())

# views to handle delete course
def delete_course(request, course_id):
    AddCourse.objects.get(pk=course_id).delete()
    return redirect('admin_page')

# views to handle adding and deleteing applicants
def add_applicant(request):
    if request.method == 'POST':
        form = StudentApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_page')
    else:
        form = StudentApplicationForm()
    return render(request, 'add_applicant.html', {'form': form})

def delete_applicant(request, applicant_id):
    StudentApplication.objects.get(pk=applicant_id).delete()
    return redirect('admin_page')


# added to route admin.html in Application/templates
def admin_page(request):
    courses = AddCourse.objects.all()
    applicants = StudentApplication.objects.all()
    return render(request, 'admin_page.html', {'courses': courses, 'applicants': applicants})

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
            return render("landingpage.html")
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
