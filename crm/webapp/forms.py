from django import forms
from phonenumber_field.formfields import PhoneNumberField

class ContactForm(forms.Form):
    first_name = forms.CharField(label='Fist Name', min_length=2)
    last_name = forms.CharField(label='Last Name', min_length=2)
    email= forms.CharField(max_length=100, widget= forms.EmailInput(attrs={'placeholder':'example@email.com'}))
    phone = PhoneNumberField(region="CA", widget=forms.TextInput(attrs={'placeholder': '(506) 234-5678'}), label="Phone Number", required=True)
    company = forms.CharField()