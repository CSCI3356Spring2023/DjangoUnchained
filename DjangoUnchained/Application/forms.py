from django import forms
from .models import StudentApplication
from .models import CourseAdd

class StudentApply(forms.ModelForm):
    class Meta:
        model = StudentApplication
        fields = ('name', 'email', 'gpa', 'gradYear', 'longAns')

class CourseAddForm(forms.ModelForm):
    class Meta:
        model = CourseAdd
        fields = ('subject', 'courseName', 'courseCode', 'instructorName', 'courseDescription', 'building', 'discussion', 'numTAs')
    