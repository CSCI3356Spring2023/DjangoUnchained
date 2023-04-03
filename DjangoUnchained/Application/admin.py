from django.contrib import admin

from .models import AddCourse, CourseAdd, StudentApplication

admin.site.register(CourseAdd)
admin.site.register(StudentApplication)
admin.site.register(AddCourse)
