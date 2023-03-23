from django import forms
from .models import StudentApplication

class StudentApply(forms.ModelForm):
    class Meta:
        model = StudentApplication
        fields = ('name', 'email', 'gpa', 'gradYear', 'longAns')
    