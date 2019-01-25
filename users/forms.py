from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import FEUser

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = FEUser
        fields = ('username','email', 'first_name', 'last_name', 'number')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = FEUser
        fields = ('username','email', 'first_name', 'last_name', 'number')
