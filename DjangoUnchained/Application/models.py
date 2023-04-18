from django.db import models

# Create your models here.

class StudentApplication(models.Model):
    """User model."""

    YEARS = (

        ('2024', '2024'),
        ('2025', '2025'),
        ('2026', '2026'),
        ('2027', '2027'),

    )
    username = None
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=200)
    gradYear = models.CharField(max_length=50, choices = YEARS, null=True)
    gpa = models.CharField(max_length=4)
    longAns = models.CharField(max_length=100000)

    #role = models.CharField(max_length=50, choices = ROLES, null=True)
    #USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = ['role', 'first_name', 'last_name']
    
    def get_full_name(self):
      return self.first_name + ' ' + self.last_name
    
    def get_email(self):
        return self.email
    
    def get_role(self):
        return self.role
    

class CourseAdd(models.Model):

    BUILDINGS = (

        ('245 Beacon', '245 Beacon'),
        ('Gasson Hall', 'Gasson Hall'),
        ('Stokes Hall', 'Stokes Hall'),
        ('Fulton Hall', 'Fulton Hall'),
        ('Lyons Hall', 'Lyons Hall'),
        ('O\'Neill', 'O\'Neill'),
        ('Higgins Hall', 'Higgins Hall'),

    )

    DAYS = (

        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),

    )

    CLASS_DAYS = (

        ('M/W/F', 'M/W/F'), 
        ('T/Th', 'T/Th'),
        ('M/W', 'M/W'),
        ('M', 'M'),
        ('T', 'T'),
        ('W', 'W'),
        ('Th', 'Th'),
        ('F', 'F'),

    )

    TIMES = (

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
        ('6:00', '6:00'),

    )

    DURATIONS = (

        ('0:50', '0:50'),
        ('1:15', '1:15'),
        ('2:30', '2:30'),

    )

    NUM_TAS = (

        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),

    )

    YES_NO = (

        ('Yes', 'Yes'),
        ('No', 'No'),

    )

    TIMES_NA = (

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

    )

    DAYS_NA = (

        ('N/A', 'N/A'),
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),

    )

    username = None
    subject = models.CharField(max_length=100)
    courseName = models.CharField(max_length=100)
    courseCode = models.CharField(max_length=100)
    courseDescription = models.CharField(max_length=1000)
    building = models.CharField(max_length=100, choices = BUILDINGS, null=True)
    days = models.CharField(max_length=100, choices = CLASS_DAYS, null=True)
    time = models.CharField(max_length=100, choices = TIMES, null=True)
    duration = models.CharField(max_length=100, choices = DURATIONS, null=True)
    numTAs = models.CharField(max_length=100, choices = NUM_TAS, null=True)
    discussion = models.CharField(max_length=100, choices = YES_NO, null=True)
    discussion_day = models.CharField(max_length=100, choices = DAYS_NA, null=True)
    discussion_time = models.CharField(max_length=100, choices = TIMES_NA, null=True)
    