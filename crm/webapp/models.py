# crm/models.py

from dataclasses import dataclass
from datetime import datetime
from django.contrib.auth.models import User

@dataclass(frozen=True)
class ContactDto:
    id: int
    last_name: str
    first_name: str
    email: str
    phone: str
    company: str
    created_at: datetime
    updated_at: datetime

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
    
    def update(self, changed):
        data = self.to_dict() | changed
        data['updated_at'] = datetime.now()
            
        return ContactDto(**data)
        
    def to_dict(self):
        return {
            "id": self.id,
            "last_name": self.last_name, 
            "first_name": self.first_name, 
            "email": self.email, 
            "phone": self.phone, 
            "company": self.company,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
        
    @staticmethod
    def get_header_names():
        return ['Name', 'Company', 'Email', 'Phone', 'Created Date', 'Modified Date']
    
    @staticmethod
    def get_field_names():
        return ['first_name last_name', 'company', 'email', 'phone', 'created_at', 'updated_at']

@dataclass(frozen=True)
class OpportunityStatusDto:
    id: int
    name: str
    
    def __str__(self):
        return self.name
    
    def to_dict(self):
        return { 
            'id': self.id,
            "name": self.name 
        }

class UserDto(User):
    def __str__(self):
        return self.username
    
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username
        }
        
@dataclass(frozen=True)
class OpportunityDto:
    id: int
    name: str
    amount: int
    user: UserDto
    contact: ContactDto
    status: OpportunityStatusDto
    opened_at: datetime
    closed_at: datetime
    
    #Override init method of the dataclass
    def __init__(self, id, name, amount, user, contact, status, opened_at, closed_at):
        object.__setattr__(self, 'id', id)
        object.__setattr__(self, 'name', name)
        object.__setattr__(self, 'amount', amount)
        object.__setattr__(self, 'user', UserDto(**user))
        object.__setattr__(self, 'contact', ContactDto(**contact))
        object.__setattr__(self, 'status', OpportunityStatusDto(**status))
        object.__setattr__(self, 'opened_at', opened_at)
        object.__setattr__(self, 'closed_at', closed_at)
        
    def __str__(self):
        return self.name
    
    @staticmethod
    def get_header_names():
        return ['Name', 'Amount', 'User', 'Contact', 'Status', 'Opened Date', 'Closed Date']
    
    @staticmethod
    def get_field_names():
        return ['name', 'amount', 'user', 'contact', 'status', 'opened_at', 'closed_at']
    
    def update(self, form):
        data = self.to_dict()
        for field in form.changed_data:
            data[field] = form.cleaned_data[field]
        return OpportunityDto(**data)
    
    def to_ref_dict(self):
        return {
            "id": self.id,
            "name": self.name, 
            "amount": self.amount, 
            "user": self.user.id, 
            "contact": self.contact.id, 
            "status": self.status.id,
            "opened_at": self.opened_at,
            "closed_at": self.closed_at
        }
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name, 
            "amount": self.amount, 
            "user": self.user.to_dict(), 
            "contact": self.contact.to_dict(),
            "status": self.status.to_dict(),
            "opened_at": self.opened_at,
            "closed_at": self.closed_at
        }

@dataclass(frozen=True)
class TaskTypeDto:
    id: int
    name: str
    
    def __str__(self):
        return self.name

    def to_dict(self):
        return { "id": self.id, "name": self.name }

@dataclass(frozen=True)
class TaskStatusDto:
    id: int
    name: str
       
    def __str__(self):
        return self.name

    def to_dict(self):
        return { "id": self.id, "name": self.name }

@dataclass(frozen=True)
class TaskDto:
    id: int
    title: str
    opportunity: OpportunityDto
    due_date: datetime
    type: TaskTypeDto
    status: TaskStatusDto

    def __init__(self, id, title, opportunity, due_date, type, status):
        object.__setattr__(self, 'id', id)
        object.__setattr__(self, 'title', title)
        object.__setattr__(self, 'opportunity', OpportunityDto(**opportunity))
        object.__setattr__(self, 'due_date', due_date)
        object.__setattr__(self, 'type', TaskTypeDto(**type))
        object.__setattr__(self, 'status', TaskStatusDto(**status))
        
    def __str__(self):
        return self.title

    def to_ref_dict(self):
        return {
            "id": self.id,
            "title": self.title, 
            "opportunity": self.opportunity_id, 
            "due_date": self.due_date, 
            "type_id": self.type_id, 
            "status_id": self.status_id 
        }
        
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title, 
            "opportunity": self.opportunity.to_dict(), 
            "due_date": self.due_date, 
            "type": self.type.to_dict(), 
            "status": self.status.to_dict() 
        }

    @staticmethod
    def get_header_names():
        return ['Title', 'Opportunity', 'Due Date', 'Type', 'Status']
    
    @staticmethod
    def get_field_names():
        return ['title', 'opportunity', 'due_date', 'type', 'status']
    
# https://github.com/radzenhq/radzen-examples/blob/master/CRMDemo/crm-database-schema.sql