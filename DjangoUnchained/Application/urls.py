from django.urls import path
from . import views

urlpatterns = [
    path('add_course/', views.add_course, name='add_course'),
    path('student_course/', views.student_course, name='student_course')
]