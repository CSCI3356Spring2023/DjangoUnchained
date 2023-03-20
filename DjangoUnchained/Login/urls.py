from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name = "landing_page"),

    path('student_login/', views.student_login, name='student_login'),
    path('instructor_login/', views.instructor_login, name='instructor_login'),
    path('administrator_login/', views.administrator_login, name='administrator_login'),
]