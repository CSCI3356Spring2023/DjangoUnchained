from django.urls import path

from . import views

urlpatterns = [
    path('', views.landing_page, name = "landing_page"),

    path('bclogin/', views.bclogin, name='bclogin'),
    path('signup/', views.signup_page, name='signup'),
]