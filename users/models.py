from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Custom User model that extends Django's AbstractUser
    to add user type functionality.
    """
    class UserType(models.TextChoices):
        JOB_SEEKER = 'job_seeker', _('Job Seeker')
        EMPLOYER = 'employer', _('Employer')
        
    email = models.EmailField(_('email address'), unique=True)
    role = models.CharField(
        max_length=20,
        choices=UserType.choices,
        default=UserType.JOB_SEEKER,
    )
    
    # Additional fields
    bio = models.TextField(blank=True)
    company_name = models.CharField(max_length=100, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'role']
    
    
    def is_employer(self):
        return self.user_type == self.UserType.EMPLOYER
    
    def is_job_seeker(self):
        return self.user_type == self.UserType.JOB_SEEKER
    
    def __str__(self):
        return self.email