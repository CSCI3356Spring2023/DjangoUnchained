from django.urls import path
from . import views

urlpatterns = [
    path('add_course/', views.add_course, name='add_course'),
    path('student_course/', views.student_course, name='student_course'),
    path('admin_page/', views.admin_page, name='admin_page'),
    path('main/', views.homepage, name="homepage"),
    path('student_apply/', views.student_apply, name='student_apply'),
    path('temp_add_course/', views.temp_add_course, name='temp_add_course'),
]