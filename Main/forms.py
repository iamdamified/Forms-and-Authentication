from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms



class UserReguistrationForm(UserCreationForm):
    email = forms.EmailField(help_text="Please enter a valid email address")

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

