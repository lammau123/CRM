from django import forms

class CustomerForm(forms.Form):
    name = forms.CharField(min_length=2)
    email = forms.EmailField()
    phone = forms.CharField()
    address = forms.CharField()