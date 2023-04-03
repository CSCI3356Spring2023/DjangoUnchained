from django.contrib import admin
from .models import StudentApplication
from .models import CourseAdd
from .models import AddCourse

admin.site.register(CourseAdd)
admin.site.register(StudentApplication)
admin.site.register(AddCourse)
