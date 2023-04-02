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
    subject = forms.CharField(required=True)
    course_name = forms.CharField(required=True)
    course_code = forms.CharField(required=True)
    course_description = forms.CharField(widget=forms.Textarea)
    building = forms.CharField(required=True)
    instructor_first_name = forms.CharField(required=True)
    instructor_last_name = forms.CharField(required=True)
    num_ta = forms.ChoiceField(choices=[(i, i) for i in range(1, 8)])
    discussion_field = forms.ChoiceField(choices=[('No', 'No'), ('Yes', 'Yes')], widget=forms.Select(attrs={'onchange': 'document.forms["course-form"].submit()'}))
    if(discussion_field == 'Yes'):
        discussion_day = forms.ChoiceField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday')], required=False)
        discussion_time = forms.ChoiceField(choices=[('Morning', 'Morning'), ('Afternoon', 'Afternoon'), ('Evening', 'Evening')], required=False)
    