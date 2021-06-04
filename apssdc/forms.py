from django import forms

from django.forms import ModelForm

from apssdc.models import update

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

class UserReg(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ['username','email']
        

        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your name'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Your Email'}),
           
        }

        
class Uppro(ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

        widgets={
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter user name'}),
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enterur  First Name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Last name'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter email id'}),

           
        }

class imagepro(forms.ModelForm):
    class Meta:
        model = update
        fields = ['image','age']

        widgets={
            'age':forms.NumberInput(attrs={'class':'form-control'})
        }

        
