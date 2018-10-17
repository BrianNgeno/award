from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Project, Profile, Rate
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user', 'pub_date', 'profile']