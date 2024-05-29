from django import forms

class CustomerForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    