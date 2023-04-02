from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
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

    form = CourseAdd()
    context = {}

    if request.method == 'POST':
        form = CourseAdd(request.POST)
        if form.is_valid():
            form.save()
    print(form)
    context['form'] = form
    return render(request, "Add_course.html", context)

def course_form(request):
    if request.method == 'POST':
        # Handle form submission
        subject = request.POST.get('subject')
        course_name = request.POST.get('course_name')
        course_code = request.POST.get('course_code')
        course_description = request.POST.get('course_description')
        building = request.POST.get('building')
        instructor_first_name = request.POST.get('instructor_first_name')
        instructor_last_name = request.POST.get('instructor_last_name')
        num_ta = request.POST.get('num_ta')
        discussion = request.POST.get('discussion')
        discussion_days = request.POST.get('discussio_days')
        discussion_times = request.POST.get('discussion_times')

        return render(request, 'course_form_discussion.html', {'subject': subject, 'course_name': course_name, 'course_code': course_code, 'course_description': course_description, 'building': building, 'instructor_first_name': instructor_first_name, 'instructor_last_name': instructor_last_name, 'num_ta': num_ta, 'discussion_days': discussion_days, 'discussion_times': discussion_times})
