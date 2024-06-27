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
    
    def changed_data_to_dict(self):
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
    
    def load(self):
        self.fields['status'].choices = (*[(-1, '----select----')], *[(status.id, status.name) for status in repos.get_opportunity_statuses()])
        self.fields['user'].choices = (*[(-1, '----select----')], *[(user.id, user.username) for user in repos.get_users()])
        self.fields['contact'].choices = (*[(-1, '----select----')], *[(contact.id, " ".join([contact.first_name, contact.last_name])) for contact in repos.get_contacts()])
        
    def changed_data_to_dict(self):
        data = {}
        
        for field in self.changed_data:
            data[field] = self.cleaned_data[field]
            
        if 'user' in data:
            data['user'] = repos.get_user_by_id(int(data['user'])).to_dict()
            
        if 'contact' in data:
            data['contact'] = repos.get_contact_by_id(int(data['contact'])).to_dict()
            
        if 'status' in data:
            data['status'] = repos.get_opportunity_status_by_id(int(data['status'])).to_dict()
            
        return data
            
class TaskForm(forms.Form):
    title = forms.CharField(min_length=2)
    opportunity = forms.ChoiceField()
    type = forms.ChoiceField()
    status =forms.ChoiceField()
    due_date = forms.DateTimeField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'type': 'date'
            }
        ),
        initial=date.today
    )
    
    def load(self):
        self.fields['opportunity'].choices = (*[(-1, '----select----')], *[(opportunity.id, opportunity.name) for opportunity in repos.get_opportunities()])
        self.fields['type'].choices = (*[(-1, '----select----')], *[(type.id, type.name) for type in repos.get_task_types()])
        self.fields['status'].choices = (*[(-1, '----select----')], *[(status.id, status.name) for status in repos.get_task_statuses()])
    
    def changed_data_to_dict(self):
        data = {}
        
        for field in self.changed_data:
            data[field] = self.cleaned_data[field]
            
        if 'opportunity' in data:
            data['opportunity'] = repos.get_opportunity_by_id(int(data['opportunity'])).to_dict()
            
        if 'type' in data:
            data['type'] = repos.get_task_type_by_id(int(data['type'])).to_dict()
            
        if 'status' in data:
            data['status'] = repos.get_task_status_by_id(int(data['status'])).to_dict()
            
        return data
        