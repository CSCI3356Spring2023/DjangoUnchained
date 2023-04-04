from django import forms
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
        use_in_migrations = True

        def _create_user(self, email, password, **extra_fields):
            """Create and save a User with the given email and password."""
            if not email:
                raise ValueError('The given email must be set')
            email = self.normalize_email(email)
            user = self.model(email=email, **extra_fields)
            user.set_password(password)
            user.save(using=self._db)
            return user

        def create_user(self, email, password=None, **extra_fields):
            """Create and save a regular User with the given email and password."""
            extra_fields.setdefault('is_staff', False)
            extra_fields.setdefault('is_superuser', False)
            return self._create_user(email, password, **extra_fields)

        def create_superuser(self, email, password, **extra_fields):
            """Create and save a SuperUser with the given email and password."""
            extra_fields.setdefault('is_staff', True)
            extra_fields.setdefault('is_superuser', True)

            if extra_fields.get('is_staff') is not True:
                raise ValueError('Superuser must have is_staff=True.')
            if extra_fields.get('is_superuser') is not True:
                raise ValueError('Superuser must have is_superuser=True.')

            return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    """User model."""

    ROLES = (

        ('Student', 'Student'),
        ('Instructor', 'Instructor'),
        ('Administrator', 'Administrator'),

    )
    username = None
    first_name =models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(_('email address'), unique=True)
    role = models.CharField(max_length=50, choices = ROLES, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['role', 'first_name', 'last_name']
    
    objects = UserManager()
    
    def get_full_name(self):
      return self.first_name + ' ' + self.last_name
    
    def get_email(self):
        return self.email
    
    def get_role(self):
        return self.role
        
    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name


class SendEmail(models.Model):

    subject = models.CharField(max_length=200, null=False, blank=False)
    body = models.TextField()
    from_email = models.CharField(max_length=200, null=False, blank=False)
    to_email = models.CharField(max_length=200, null=False, blank=False)
    
    def get_subject(self):
      return self.subject
    
    def get_body(self):
        return self.body
    
    def get_from_email(self):
        return self.from_email
    
    def get_to_email(self):
        return self.to_email