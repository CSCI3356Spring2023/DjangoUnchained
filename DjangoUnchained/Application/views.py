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

    name = request.POST.get('name')
    gradYear = request.POST.get('gradYear')
    gpa = request.POST.get('gpa')
    longAns = request.POST.get('longAns')

    print(name, gradYear, gpa, longAns)
   
    return render(request, "studentApply.html")
