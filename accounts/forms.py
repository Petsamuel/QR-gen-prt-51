from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import CustomUser

class SignUpForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('full_name', 'email')


class LogInForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)