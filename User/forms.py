from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Custom_User

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = Custom_User
        fields = ['username', 'email', 'password1', 'password2', 'role', 'birth_date']

class AssignRoleForm(forms.ModelForm):
    class Meta:
        model = Custom_User
        fields = ['role']
