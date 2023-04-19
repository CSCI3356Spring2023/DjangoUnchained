from django import forms
from .models import StudentApplication
from .models import CourseAdd
from django.core.validators import MaxValueValidator, MinValueValidator

class StudentApply(forms.ModelForm):
    class Meta:
        model = StudentApplication
        fields = ('name', 'email', 'gpa', 'gradYear', 'longAns')

class CourseAddForm(forms.ModelForm):
    buildings = [
        ('placeholder', 'Building'),
        ('245 Beacon', '245 Beacon'),
        ('Gasson Hall', 'Gasson Hall'),
        ('Stokes Hall', 'Stokes Hall'),
        ('Fulton Hall', 'Fulton Hall'),
        ('Lyons Hall', 'Lyons Hall'),
        ('O\'Neill', 'O\'Neill'),
        ('Higgins Hall', 'Higgins Hall')
    ]

    days_choices = [
        ('placeholder', 'Section Days'),
        ('M/W/F', 'M/W/F'),
        ('T/Th', 'T/Th'),
        ('M/W', 'M/W'),
        ('M', 'M'),
        ('T', 'T'),
        ('W', 'W'),
        ('Th', 'Th'),
        ('F', 'F')
    ]

    class_times = [
        ('placeholder', 'Section Time'),
        ('9:00', '9:00'),
        ('9:30', '9:30'),
        ('10:00', '10:00'),
        ('10:30', '10:30'),
        ('11:00', '11:00'),
        ('11:30', '11:30'),
        ('12:00', '12:00'),
        ('12:30', '12:30'),
        ('1:00', '1:00'),
        ('1:30', '1:30'),
        ('2:00', '2:00'),
        ('2:30', '2:30'),
        ('3:00', '3:00'),
        ('3:30', '3:30'),
        ('4:00', '4:00'),
        ('4:30', '4:30'),
        ('5:00', '5:00'),
        ('5:30', '5:30'),
        ('6:00', '6:00'),
        ('6:30', '6:30'),
        ('7:00', '7:00'),
    ]

    durations = [
        ('placeholder', 'Class Duration'),
        ('0:50', '0:50'),
        ('1:15', '1:15'),
        ('2:30', '2:30'),
    ]

    numTA_Choices = [
        ('placeholder', 'Number of TAs Needed'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
    ]
    
    discussion_choices = [
        ('placeholder', 'Discussion Section?'),
        ('Yes', 'Yes'),
        ('No', 'No')
    ]

    discussion_days = [
        ('placeholder', 'Discussion Day'),
        ('N/A', 'N/A'),
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
    ]

    discussion_times = [
        ('placeholder', 'Discussion Time'),
        ('N/A', 'N/A'),
        ('9:00', '9:00'),
        ('9:30', '9:30'),
        ('10:00', '10:00'),
        ('10:30', '10:30'),
        ('11:00', '11:00'),
        ('11:30', '11:30'),
        ('12:00', '12:00'),
        ('12:30', '12:30'),
        ('1:00', '1:00'),
        ('1:30', '1:30'),
        ('2:00', '2:00'),
        ('2:30', '2:30'),
        ('3:00', '3:00'),
        ('3:30', '3:30'),
        ('4:00', '4:00'),
        ('4:30', '4:30'),
        ('5:00', '5:00'),
        ('5:30', '5:30'),
        ('6:00', '6:00'),
        ('6:30', '6:30'),
        ('7:00', '7:00'),
    ]

    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Subject', 'class': 'short_text'}))
    courseName = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Course Name', 'class': 'short_text'}))
    courseCode = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Course Code', 'class': 'short_text'}))
    courseDescription = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Course Description', 'class': 'class_description'}))
    building = forms.CharField(widget=forms.Select(choices=buildings))
    days = forms.CharField(widget=forms.Select(choices=days_choices))
    time = forms.CharField(widget=forms.Select(choices=class_times))
    duration = forms.CharField(widget=forms.Select(choices=durations))
    numTas = forms.CharField(widget=forms.Select(choices=numTA_Choices))
    discussion = forms.CharField(widget=forms.Select(choices=discussion_choices))
    discussion_day = forms.CharField(widget=forms.Select(choices=discussion_days))
    discussion_time = forms.CharField(widget=forms.Select(choices=discussion_times))
    
    class Meta:
        model = CourseAdd
        fields = ['subject', 'courseName', 'courseCode', 'courseDescription', 'building', 'days', 'time', 'duration', 'numTAs', 'discussion', 'discussion_day', 'discussion_time']
    