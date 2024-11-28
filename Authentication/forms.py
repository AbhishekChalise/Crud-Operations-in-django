from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import transaction
from .models import Custom_User


class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = Custom_User
        fields = ['username','email','password1','password2']


class AssignRoleForm(forms.ModelForm):
    class Meta:
        model = Custom_User
        fields = ['role']