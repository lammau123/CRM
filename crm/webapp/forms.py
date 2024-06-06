from django import forms
from .models import ContactDto

class ContactForm(forms.Form):
    first_name = forms.CharField(label='Fist Name', min_length=2)
    last_name = forms.CharField(label='Last Name', min_length=2)
    email = forms.EmailField()
    phone = forms.CharField()
    company = forms.CharField()