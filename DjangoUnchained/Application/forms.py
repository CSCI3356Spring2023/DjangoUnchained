from django import forms
from .models import StudentApplication
from .models import CourseAdd

class StudentApply(forms.ModelForm):
    class Meta:
        model = StudentApplication
        fields = ('name', 'email', 'gpa', 'gradYear', 'longAns')

class CourseAdd(forms.ModelForm):
    class Meta:
        model = CourseAdd
        fields = ('courseName', 'courseCode', 'instructorName', 'courseDescription', 'building', 'discussion', 'numTAs')
    