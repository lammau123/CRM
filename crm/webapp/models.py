# crm/models.py

from dataclasses import dataclass
from datetime import datetime

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
        return {"last_name": self.last_name, "first_name": self.first_name, "email": self.email, "phone": self.phone, "company": self.company}

@dataclass(frozen=True)
class TaskType:
    name: str
    
    def __str__(self):
        return self.name

@dataclass(frozen=True)
class TaskStatus:
    name: str
    
    def __str__(self):
        return self.name

@dataclass(frozen=True)
class Task:
    title: str
    opportunity_id: int
    due_date: datetime
    type_id: int
    status_id: int

    def __str__(self):
        return self.title

@dataclass(frozen=True)
class OpportunityStatus:
    name: str
    
    def __str__(self):
        return self.name
    
@dataclass(frozen=True)
class Opportunity:
    name: str
    amount: int
    user_id: int
    contact_id: int
    status_id: int
    open_date: datetime
    close_date: datetime
    
    def __str__(self):
        return self.name
    
# https://github.com/radzenhq/radzen-examples/blob/master/CRMDemo/crm-database-schema.sql