from django import forms
from .models import AddCourse, StudentApplication
from .models import CourseAdd

class StudentApply(forms.ModelForm):
    class Meta:
        model = StudentApplication
        fields = ('name', 'email', 'gpa', 'gradYear', 'longAns')

class CourseAdd(forms.ModelForm):
    class Meta:
        model = CourseAdd
        fields = ('subject', 'courseName', 'courseCode', 'instructorName', 'courseDescription', 'building', 'discussion', 'numTAs')

class AddCourse(forms.ModelForm):
    class Meta:
        model = AddCourse
        fields = ('subject', 'course_name', 'course_code', 'course_description', 'building', 'class_day', 'class_time','instructor_first_name','instructor_last_name','num_ta','discussion_field','discussion_day','discussion_time')