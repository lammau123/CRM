from django import forms
from phonenumber_field.formfields import PhoneNumberField
from .repository import repositories as repos

class ContactForm(forms.Form):
    first_name = forms.CharField(label='Fist Name', min_length=2)
    last_name = forms.CharField(label='Last Name', min_length=2)
    email= forms.CharField(max_length=100, widget= forms.EmailInput(attrs={'placeholder':'example@email.com'}))
    phone = PhoneNumberField(region="CA", widget=forms.TextInput(attrs={'placeholder': '(506) 234-5678'}), label="Phone Number", required=True)
    company = forms.CharField()
    
    
class OpportunityForm(forms.Form):
    name = forms.CharField(label='Name', min_length=2)
    amount = forms.DecimalField()
    user = forms.ChoiceField()
    contact = forms.ChoiceField()
    status = forms.ChoiceField()
    
    async def load(self):
        self.fields['status'].choices = (*[(-1, '----select----')], *[(status.id, status.name) for status in await repos.get_opportunity_statuses()])
        self.fields['user'].choices = (*[(-1, '----select----')], *[(user.id, user.username) for user in await repos.get_users()])
        self.fields['contact'].choices = (*[(-1, '----select----')], *[(contact.id, " ".join([contact.first_name, contact.last_name])) for contact in await repos.get_contacts()])