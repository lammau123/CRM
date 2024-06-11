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
    
    def toDict(self):
        return {
            "last_name": self.last_name, 
            "first_name": self.first_name, 
            "email": self.email, 
            "phone": self.phone, 
            "company": self.company
        }
        
    @staticmethod
    def get_header_names():
        return ['Name', 'Company', 'Email', 'Phone', 'Created Date', 'Modified Date']
    
    @staticmethod
    def get_field_names():
        return ['first_name last_name', 'company', 'email', 'phone', 'created_at', 'updated_at']

@dataclass(frozen=True)
class TaskTypeDto:
    name: str
    
    def __str__(self):
        return self.name

    def toDict(self):
        return { "name": self.name }

@dataclass(frozen=True)
class TaskStatusDto:
    name: str
       
    def __str__(self):
        return self.name

    def toDict(self):
        return { "name": self.name }

@dataclass(frozen=True)
class TaskDto:
    title: str
    opportunity_id: int
    due_date: datetime
    type_id: int
    status_id: int

    def __str__(self):
        return self.title

    def toDict(self):
        return {
            "title": self.title, 
            "opportunity": self.opportunity_id, 
            "due_date": self.due_date, 
            "type_id": self.type_id, 
            "status_id": self.status_id 
        }

@dataclass(frozen=True)
class OpportunityStatusDto:
    id: int
    name: str
    
    def __str__(self):
        return self.name
    
    def toDict(self):
        return { "name": self.name }

class UserDto(User):
    def __str__(self):
        return self.username
        
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
    
    def __str__(self):
        return self.name
    
    @staticmethod
    def get_header_names():
        return ['Name', 'Amount', 'User', 'Contact', 'Status', 'Opened Date', 'Closed Date']
    
    @staticmethod
    def get_field_names():
        return ['name', 'amount', 'user', 'contact', 'status', 'opened_at', 'closed_at']
    
    def toDict(self):
        return {
            "name": self.name, 
            "amount": self.amount, 
            "user": self.user, 
            "contact_id": self.contact, 
            "status_id": self.status, 
            "opened_at": self.opened_at,
            "closed_at": self.closed_at
        }

# https://github.com/radzenhq/radzen-examples/blob/master/CRMDemo/crm-database-schema.sql