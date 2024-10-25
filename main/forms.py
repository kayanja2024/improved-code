from django import forms
from .models import patiant_data
from .models import Patient
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User



class DataForm(forms.ModelForm):
    
    class Meta:
        model = patiant_data

        fields = '__all__'


class PatientForm(forms.ModelForm):
    
    class Meta:
        model = Patient

        fields = '__all__'


class Sign_upForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    contact = forms.CharField()

    class Meta:
        model = User
        fields = ["first_name","last_name","contact","username","password1","password2"]



