from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

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
    
@csrf_exempt
def student_apply(request):

    string1 = str(request.body)

    test = string1.split('&')

    arr = []

    for string in test:
        arr.append(string.split('=')[1])

    arr[len(arr) - 1] = arr[len(arr) - 1][:-1]

    name = arr[0]
    email = arr[1]
    gradYear = arr[2]
    gpa = arr[3]
    longAns = arr[4]

    print('Name: ', name)
    print('Email: ', email)
    print('Graduation Year', gradYear)
    print('GPA: ', gpa)
    print('Why do you want to TA for this class?: ', longAns)
    

    #print(request.body[0])

    #if request.method == 'POST':
        #name = request.get('name')
        #gradYear = request.get('gradYear')
        #gpa = request.get('gpa')
        #longAns = request.get('longAns')
        #print(request.GET)

    


    #print(name, gradYear, gpa, longAns)

    return render(request, "studentApply.html")

