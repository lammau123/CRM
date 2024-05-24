from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput
from .models import CustomerRecord

# register a user
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        
# login form
class LoginForn(AuthenticationForm):
    username = forms.CharField(widget=PasswordInput())
    password = forms.CharField(widget=PasswordInput())
    
class CreateCustomerForm(forms.ModelForm):
    class Meta:
        model = CustomerRecord
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'province', 'country']
        
class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model = CustomerRecord
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'province', 'country']
        