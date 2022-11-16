from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import  Dashboard


class SignUpForm(UserCreationForm):
    password2=forms.CharField(widget=forms.PasswordInput,label='confirm password(again)')

    class Meta:
        model=User
        fields=['username','first_name','last_name','email']


class Contact(forms.Form):
    Name = forms.CharField(max_length=30)
    email= forms.EmailField()
    MobileNo = forms.IntegerField()
    City = forms.CharField(max_length=10)

class Dashboardform(forms.ModelForm):
    class Meta:
        model = Dashboard
        fields= '__all__'





