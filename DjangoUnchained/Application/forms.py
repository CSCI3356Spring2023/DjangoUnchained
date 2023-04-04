from django import forms

from .models import AddCourse, StudentApplication


class StudentApply(forms.ModelForm):
    class Meta:
        model = StudentApplication
        fields = ('name', 'email', 'gpa', 'gradYear', 'longAns')

class AddCourse(forms.ModelForm):
    class Meta:
        model = AddCourse
        fields = ('subject', 'course_name', 'course_code', 'course_description', 'building', 'class_day', 'class_time','instructor_first_name','instructor_last_name','num_ta','discussion_field','discussion_day','discussion_time')
        
        
# added to test admin page
class AddCourseForm(forms.ModelForm):
    class Meta:
        model = AddCourse
        fields = '__all__'

class StudentApplicationForm(forms.ModelForm):
    class Meta:
        model = StudentApplication
        fields = '__all__'
