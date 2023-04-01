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
        fields = ('subject', 'courseName', 'courseCode', 'instructorName', 'courseDescription', 'building', 'discussion', 'numTAs')

class TAForm(forms.Form):
    number_of_TAs = forms.ChoiceField(choices=[(i, i) for i in range(1, 8)])
    discussion_field = forms.ChoiceField(choices=[('Yes', 'Yes'), ('No', 'No')], widget=forms.RadioSelect)


    