from django import forms
from eapp.models import Employeetask
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EmployeetaskModelForm(forms.ModelForm):
    name=forms.CharField(max_length=50) 
    cat=forms.IntegerField()
    status=forms.BooleanField()


    class Meta:
      model=Employeetask 
      fields=['name','cat','status'] 

class UserForm(UserCreationForm):

    class Meta:
        model=User
        fields=['username','first_name','last_name','email']      