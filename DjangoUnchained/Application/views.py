from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from .forms import StudentApply
from .forms import CourseAddForm
from django.shortcuts import get_object_or_404, redirect
from django.core import mail

from .models import CourseAdd
from .models import StudentApplication

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

def num_fulfilled_TA(queryset):
    count = 0
    TAs = 0
    for i in queryset:
        if i.fulfilled == "Yes":
            count += 1
        else:
            TAs += int(i.numTAs) - int(i.currTAs)
    return count, TAs
# added to route admin.html in Application/templates
def admin_page(request):
    if request.user.is_authenticated:
        userInfo = request.user
        firstName = userInfo.get_first_name()
        lastName = userInfo.get_last_name()
        userRole = request.user.get_role()
        if (userRole == "Administrator"):
            courseInfo = CourseAdd.objects.all()
            applicantInfo = StudentApplication.objects.all()
            fulfilled_courses, TAneeded = num_fulfilled_TA(courseInfo)
            not_filled_courses = len(courseInfo) - fulfilled_courses
            context = {'Courses': courseInfo, 'Applicants': applicantInfo, 'Users': userInfo, 'FirstName': firstName, 'LastName': lastName,
                       'Applicant_Number': len(applicantInfo), 'Course_Number': len(courseInfo), 'Fulfilled': fulfilled_courses,
                       'Not_Fulfilled': not_filled_courses, 'TAs': TAneeded}

            return render(request, 'admin_page.html', context)
        else:
            return render(request, '404.html')
    else:
        return render(request, '404.html')

def instructor_page(request):
    if request.user.is_authenticated:
        userInfo = request.user
        firstName = userInfo.get_first_name()
        lastName = userInfo.get_last_name()

        userRole = request.user.get_role()
        if (userRole == "Instructor"):
            courseInfo = CourseAdd.objects.filter(instructor=userInfo.get_full_name())
            applicantInfo = StudentApplication.objects.all()
            #need to edit
            fulfilled_courses, TAneeded = num_fulfilled_TA(courseInfo)
            #need to edit
            not_filled_courses = len(courseInfo) - fulfilled_courses
            context = {'Courses': courseInfo, 'Applicants': applicantInfo, 'Users': userInfo, 'FirstName': firstName, 'LastName': lastName,
                       'Applicant_Number': len(applicantInfo), 'Course_Number': len(courseInfo), 'TAs': TAneeded}

            return render(request, 'instructor_visual.html', context)
        else: 
            return render(request, '404.html')
    else:
        return render(request, '404.html')
    
def homepage(request):
    if request.user.is_authenticated:
        userRole = request.user.get_role()
        if (userRole == 'Student'):
            return student_page(request)
        elif (userRole == 'Instructor'):
            return instructor_page(request)
        elif (userRole == 'Administrator'):
            return admin_page(request)
        else:
            return render(request, "homepage.html")
        
    else:
        return render(request, "landingpage.html")


def temp_add_course(request):

    form = CourseAddForm()
    if request.user.is_authenticated:
        userRole = request.user.get_role()
        if (userRole == 'Instructor' or userRole == "Administrator"):
            if request.method == 'POST':
                form = CourseAddForm(request.POST)
                # CODE FOR CHANGING DATA
                data = request.POST
                data._mutable = True
                data['fulfilled'] = "No"
                data['currTAs'] = 0
                data._mutable = False
                #CODE ABOVE FOR CHANGING DATA
                if form.is_valid():
                    form.save()
                    return redirect('/main')  # Redirect to the main page after successful form submission
                else:
                    # Render the form with error messages if it's not valid
                    return render(request, 'temp_add_course.html', {'form': form})
            else:
                form = CourseAddForm()
                return render(request, 'temp_add_course.html', {'form': form})
        else:
            return render(request, '404.html')
    else:
        return render(request, '404.html')

def student_page(request):
    if request.user.is_authenticated:
        userRole = request.user.get_role()
        userInfo = request.user
        firstName = userInfo.get_first_name()
        lastName = userInfo.get_last_name()
        applicantInfo = StudentApplication.objects.filter(email = userInfo.get_email())
        courseInfo = CourseAdd.objects.all()
        appliedCourses, getResults = get_applied_courses(applicantInfo, courseInfo)
        allInfo = []
        for i in range(len(appliedCourses)):
            allInfo.append([appliedCourses[i], getResults[i]])
        numOfTAs = len(allInfo)
        if(userRole == "Student"):
            context = {'Users': userInfo, 'FirstName': firstName, 'LastName': lastName, 'Courses': courseInfo, 'Applications': allInfo, "NumberTA": numOfTAs}
            return render(request, 'studentTAapplication.html', context)
    return render(request, '404.html')

def get_applied_courses(applicantInfo, courseInfo):
    appliedCourses = []
    getResult = []
    for i in range(len(applicantInfo)):
        name = applicantInfo[i].courseName
        appliedCourses.append(name)
        result = applicantInfo[i].results
        getResult.append(result)

    return courseInfo.filter(courseName__in=appliedCourses), getResult

def course_list(request):
    if request.user.is_authenticated:
    #template = loader.get_template('course_list.html')]
        courseInfo = CourseAdd.objects.all()
        courses = {'Courses': courseInfo}
        #return HttpResponse(template.render(courses, request))

        return render(request, 'course_list.html', courses)
    return render(request, '404.html')

def delete_course(request, course_id):
    course = get_object_or_404(CourseAdd, id=course_id)
    course.delete()
    return redirect('admin_page')  # Redirect to the admin_page or the page where you display the list of courses


def delete_applicant(request, applicant_id):
    applicant = get_object_or_404(StudentApplication, id=applicant_id)
    applicant.delete()
    return redirect('admin_page')  # Redirect to the admin_page or the page where you display the list of courses

def accept_applicant(request, applicant_id):
    userRole = request.user.get_role()
    applicant = get_object_or_404(StudentApplication, id=applicant_id)
    applicant.set_results("Accepted")
    emailAddress = applicant.email
    print(emailAddress)
    body = "Congrats. You've accepted as a TA!"
    send_email(body, emailAddress)
    if userRole == "Administrator": 
        return redirect('admin_page') # Redirect to the admin_page or the page where you display the list of courses
    if userRole == "Administrator": 
        return redirect('instructor_page')  # Redirect to the instructor_page or the page where you display the list of courses

def deny_applicant(request, applicant_id):
    userRole = request.user.get_role()
    applicant = get_object_or_404(StudentApplication, id=applicant_id)
    applicant.set_results("Denied")
    emailAddress = applicant.email
    print(emailAddress)
    body = "Sorry, unfortunately you were not selected as a TA."
    send_email(body, emailAddress)
    if userRole == "Administrator": 
        return redirect('admin_page') # Redirect to the admin_page or the page where you display the list of courses
    if userRole == "Administrator": 
        return redirect('instructor_page')  # Redirect to the instructor_page or the page where you display the list of courses

def application_list(request):

    #template = loader.get_template('application_list.html')
    email = request.user.get_email()
    coursesAppliedTo = StudentApplication.objects.filter(StudentApplication.get_email==email)

    applications = {'Applications': coursesAppliedTo}

    #return HttpResponse(template.render(applications, request))

    return render(request, 'application_list.html', applications)

def edit_course(request, course_id): 

    if request.user.is_authenticated:
        userRole = request.user.get_role()
        if (userRole == 'Instructor' or userRole == "Administrator"):

            course = get_object_or_404(CourseAdd, id=course_id)

            # If they fill out the form and click the button they're posting
            # Otherwise just put the form up
            # instance loads up the form with values from course
            form = CourseAddForm(request.POST or None, instance=course)

            if form.is_valid(): 
                form.save()
                if (userRole == 'Instructor'):
                    return redirect('instructor_visual.html')
                return redirect('admin_page')

            return render(request, 'edit_course.html', {'course': course, 'form': form})
        
        else:
            return render(request, '404.html')
    else:
        return render(request, '404.html')
    

def student_apply(request, course_id):
    if request.user.is_authenticated:
        userRole = request.user.get_role()
        if(userRole == 'Student' or userRole =="Administrator"):
            form = StudentApply()
            course = get_object_or_404(CourseAdd, id=course_id)
            if request.method == 'POST':
                form = StudentApply(request.POST)
                # CODE FOR CHANGING DATA
                data = request.POST
                data._mutable = True
                data['results'] = "Pending"
                data._mutable = False
                #CODE ABOVE FOR CHANGING DATA
                print("hmmm")
                if form.is_valid():
                    print("yay")
                    my_instance = form.save(commit=False)
                    my_instance.instructor = course.instructor
                    my_instance.courseName = course.courseName
                    my_instance.save()
                    form.save()
                    return redirect('/main')  # Redirect to the main page after successful form submission
        
            return render(request, "studentApply.html", {'form': form, 'course': course})
        
        else:
            return render(request, '404.html')
    else:
        return render(request, '404.html')

def send_email(body, emailAddress):
    connection = mail.get_connection()
    connection.open()
    email = mail.EmailMessage("TA Application Status Update", body, 'djangounchainedtest@outlook.com', [emailAddress], connection=connection)
    email.send()
    connection.close()
    return 