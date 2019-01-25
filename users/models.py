from django.contrib.auth.models import AbstractUser
from django.db import models

class FEUser(AbstractUser):
    number = models.CharField(max_length=30)
    email = models.EmailField(('email address'), unique=True)
    first_name = models.CharField(('first name'), max_length=30, blank=True)
    last_name = models.CharField(('last name'), max_length=30, blank=True)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

    def getNumber(self):
        return self.number

    def getEmail(self):
        return self.email
