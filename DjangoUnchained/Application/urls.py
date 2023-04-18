from django.urls import path

from . import views


urlpatterns = [
    path('add_course/', views.temp_add_course, name='temp_add_course'),
    path('student_course/', views.student_course, name='student_course'),
    path('admin_page/', views.admin_page, name='admin_page'),
    path('main/', views.homepage, name="homepage"),
    path('student_apply/', views.student_apply, name='student_apply'),
    path('course_list/', views.course_list, name='course_list'),
    path('delete_course/<int:course_id>/', views.delete_course, name='delete_course'),
]