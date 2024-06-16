from django import forms
from phonenumber_field.formfields import PhoneNumberField
from .repository import repositories as repos
from datetime import date

class ContactForm(forms.Form):
    first_name = forms.CharField(label='Fist Name', min_length=2)
    last_name = forms.CharField(label='Last Name', min_length=2)
    email= forms.CharField(max_length=100, widget= forms.EmailInput(attrs={'placeholder':'example@email.com'}))
    phone = PhoneNumberField(region="CA", widget=forms.TextInput(attrs={'placeholder': '(506) 234-5678'}), label="Phone Number", required=True)
    company = forms.CharField()
    
    def to_dict(self):
        data = {}
        
        for field in self.changed_data:
            data[field] = self.cleaned_data[field]
            
        return data
    
    
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
        
    async def to_dict(self):
        data = {}
        
        for field in self.changed_data:
            data[field] = self.cleaned_data[field]
            
        if 'user' in data:
            data['user'] = (await repos.get_user_by_id(int(data['user']))).to_dict()
            
        if 'contact' in data:
            data['contact'] = (await repos.get_contact_by_id(int(data['contact']))).to_dict()
            
        if 'status' in data:
            data['status'] = (await repos.get_opportunity_status_by_id(int(data['status']))).to_dict()
            
        return data
            
class TaskForm(forms.Form):
    title = forms.CharField(min_length=2)
    opportunity = forms.ChoiceField()
    due_date = forms.DateTimeField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'type': 'date'
            }
        ),
        initial=date.today
    )
    type = forms.ChoiceField()
    status =forms.ChoiceField()
    
    async def load(self):
        self.fields['opportunity'].choices = (*[(-1, '----select----')], *[(opportunity.id, opportunity.name) for opportunity in await repos.get_opportunities()])
        self.fields['type'].choices = (*[(-1, '----select----')], *[(type.id, type.name) for type in await repos.get_task_types()])
        self.fields['status'].choices = (*[(-1, '----select----')], *[(status.id, status.name) for status in await repos.get_task_statuses()])
    
    async def to_dict(self):
        data = {}