from django.contrib import admin

from .models import CustomUser

from django.shortcuts import render


@admin.action(description='Send Email')
def send_email(modeladmin, request, queryset):
    connection = mail.get_connection()
    connection.open()
    for user in queryset:
        email = mail.EmailMessage("Test Subject", "Test Body", 'djangounchainedtest@outlook.com', 
                                  [user.email], connection=connection)
        email.send()
    
    connection.close()
    return render(request, 'send_email.html', context={})

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'role']
    actions = [send_email]


admin.site.register(CustomUser, CustomUserAdmin)
