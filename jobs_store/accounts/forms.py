from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'location', 'birth_date', 'job', 'skills']

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Requis. Renseignez une adresse email valide.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    
