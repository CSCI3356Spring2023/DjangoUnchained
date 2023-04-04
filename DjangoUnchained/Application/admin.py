from django.contrib import admin

from .models import AddCourse, StudentApplication

admin.site.register(StudentApplication)
admin.site.register(AddCourse)
