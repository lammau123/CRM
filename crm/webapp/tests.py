#from django.test import TestCase

from dataclasses import dataclass

@dataclass(frozen=True)
class UserDto:
    first_name: str
    last_name: str
    
    def to_dict(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name
        }
    
# Create your tests here.
@dataclass(frozen=True)
class OpportunityDto:
    id: int
    name: str
    amount: int
    user: UserDto
    t: str

    #Override init method of the dataclass
    def __init__(self, id, name, amount, user, t):
        object.__setattr__(self, 'id', id)
        object.__setattr__(self, 'name', name)
        object.__setattr__(self, 'amount', amount)
        object.__setattr__(self, 'user', UserDto(**user))
        object.__setattr__(self, 't', t)
            
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name, 
            "amount": self.amount, 
            "user": self.user.to_dict()
        }
        
    #def update(self):
        


data = {
    'id': 1,
    'name': 'name1',
    'amount': 123,
    'user': {
        'first_name': 'fff',
        'last_name': 'fff'
    },
    't': 'ssss'
}

f = OpportunityDto(**data)

print(f.to_dict())