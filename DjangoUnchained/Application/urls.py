from django.urls import path

from . import views


urlpatterns = [
    path('add_course/', views.temp_add_course, name='temp_add_course'),
    path('student_course/', views.student_course, name='student_course'),
    path('admin_page/', views.admin_page, name='admin_page'),
    path('main/', views.homepage, name="homepage"),
    path('student_apply/<int:course_id>/', views.student_apply, name='student_apply'),
    path('course_list/', views.course_list, name='course_list'),
    path('delete_course/<int:course_id>/', views.delete_course, name='delete_course'),
    path('delete_applicant/<int:applicant_id>/', views.delete_applicant, name='delete_applicant'),
    path('accept_applicant/<int:applicant_id>/', views.accept_applicant, name='accept_applicant'),
    path('deny_applicant/<int:applicant_id>/', views.deny_applicant, name='deny_applicant'),
    path('application_list/', views.application_list, name='application_list'),
    path('edit_course/<int:course_id>/', views.edit_course, name='edit_course'),
    path('offer_role/', views.offer_role, name='offer_role'),
]