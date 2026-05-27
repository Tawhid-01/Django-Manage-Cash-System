from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm


class RegisterForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
     super().__init__(*args, **kwargs)

     for i_name, i in self.fields.items():
         i.widget.attrs['class'] = 'form-control'
    

class LoginForm(AuthenticationForm):
    class Meta:
        model = UserModel
        fields = ['username', 'password1']

    def __init__(self, *args, **kwargs):
     super().__init__(*args, **kwargs)

     for i_name, i in self.fields.items():
         i.widget.attrs['class'] = 'form-control'    


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['full_name', 'occupation', 'address', 'image']
    
    def __init__(self, *args, **kwargs):
     super().__init__(*args, **kwargs)

     for i_name, i in self.fields.items():
         i.widget.attrs['class'] = 'form-control'

        



class AddCashForm(forms.ModelForm):
    class Meta:
        model = AddCashModel
        fields = ['amount', 'source']

    def __init__(self, *args, **kwargs):
     super().__init__(*args, **kwargs)

     for i_name, i in self.fields.items():
         i.widget.attrs['class'] = 'form-control'


class ExpendCashForm(forms.ModelForm):
    class Meta:
        model = ExpendCashModel
        fields = ['amount', 'destination']
    
    def __init__(self, *args, **kwargs):
     super().__init__(*args, **kwargs)

     for i_name, i in self.fields.items():
         i.widget.attrs['class'] = 'form-control'