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
    

class AddCourse(models.Model):
    """User model."""

    YEARS = (

        ('2024', '2024'),
        ('2025', '2025'),
        ('2026', '2026'),
        ('2027', '2027'),

    )

    subject = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=100)
    course_description = models.CharField(max_length=100)
    building = models.CharField(max_length=100)
    class_day = models.CharField(max_length=100)
    class_time = models.CharField(max_length=100)
    instructor_first_name = models.CharField(max_length=100)
    instructor_last_name = models.CharField(max_length=100)
    num_ta = models.CharField(max_length=100)
    discussion_field = models.CharField(max_length=100)
    discussion_day = models.CharField(max_length=100)
    discussion_time = models.CharField(max_length=100)
    
    def get_full_name(self):
      return self.first_name + ' ' + self.last_name
    
    def get_email(self):
        return self.email
    
    def get_role(self):
        return self.role