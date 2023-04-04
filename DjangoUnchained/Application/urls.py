from django.urls import path

from . import views

urlpatterns = [
    path('add_course/', views.add_course, name='add_course'),
    path('student_course/', views.student_course, name='student_course'),
    path('admin_page/', views.admin_page, name='admin_page'),
    # path('delete_course/<int:course_id>/', views.delete_course, name='delete_course'),
    # path('add_applicant/', views.add_applicant, name='add_applicant'),
    # path('delete_applicant/<int:applicant_id>/', views.delete_applicant, name='delete_applicant'),
    path('main/', views.homepage, name="homepage"),
    path('student_apply/', views.student_apply, name='student_apply'),
    path('Add_course/', views.Add_course, name='add_course'),
]