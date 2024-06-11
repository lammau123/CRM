from ..models import ContactDto, OpportunityDto, UserDto, OpportunityStatusDto
from datetime import datetime

list_of_users = [
        UserDto(id=1, username='Test1'),
        UserDto(id=2, username='Test2'),
        UserDto(id=3, username='Test3'),
        UserDto(id=4, username='Test3'),
        UserDto(id=5, username='Test3'),
]

list_of_statuses = [
        OpportunityStatusDto(id=1, name='status1'),
        OpportunityStatusDto(id=2, name='status2'),
        OpportunityStatusDto(id=3, name='status3'),
        OpportunityStatusDto(id=4, name='status4'),
        OpportunityStatusDto(id=5, name='statuss5'),
]

list_of_contacts = [
        ContactDto(id=1, first_name='first', last_name='last', phone='123-123-123', company='123 ooo st', email="asd@gmail.com", created_at=datetime(2024, 5, 21, 9, 0, 0), updated_at=datetime(2024, 5, 21, 9, 0, 0)),
        ContactDto(id=1, first_name='first', last_name='last', phone='123-123-123', company='123 ooo st', email="asd@gmail.com", created_at=datetime(2024, 5, 21, 9, 0, 0), updated_at=datetime(2024, 5, 21, 9, 0, 0)),
        ContactDto(id=1, first_name='first', last_name='last', phone='123-123-123', company='123 ooo st', email="asd@gmail.com", created_at=datetime(2024, 5, 21, 9, 0, 0), updated_at=datetime(2024, 5, 21, 9, 0, 0)),
        ContactDto(id=1, first_name='first', last_name='last', phone='123-123-123', company='123 ooo st', email="asd@gmail.com", created_at=datetime(2024, 5, 21, 9, 0, 0), updated_at=datetime(2024, 5, 21, 9, 0, 0)),
        ContactDto(id=1, first_name='first', last_name='last', phone='123-123-123', company='123 ooo st', email="asd@gmail.com", created_at=datetime(2024, 5, 21, 9, 0, 0), updated_at=datetime(2024, 5, 21, 9, 0, 0)),
    ]



list_of_opportunities = [
        OpportunityDto(
            id=1,
            name='Opportunity 1', 
            amount='12', 
            user=list_of_users[0], 
            contact=list_of_contacts[0], 
            status=list_of_statuses[0], 
            opened_at=datetime(2024, 5, 21, 9, 0, 0), 
            closed_at=datetime(2024, 5, 21, 9, 0, 0)),
        OpportunityDto(
            id=2,
            name='Opportunity 2', 
            amount='12', 
            user=list_of_users[1], 
            contact=list_of_contacts[1], 
            status=list_of_statuses[1], 
            opened_at=datetime(2024, 5, 21, 9, 0, 0), 
            closed_at=datetime(2024, 5, 21, 9, 0, 0)),
        OpportunityDto(
            id=3,
            name='Opportunity 3', 
            amount='12', 
            user=list_of_users[2], 
            contact=list_of_contacts[2], 
            status=list_of_statuses[2], 
            opened_at=datetime(2024, 5, 21, 9, 0, 0), 
            closed_at=datetime(2024, 5, 21, 9, 0, 0)),
        OpportunityDto(
            id=4,
            name='Opportunity 4', 
            amount='12', 
            user=list_of_users[3], 
            contact=list_of_contacts[3], 
            status=list_of_statuses[3], 
            opened_at=datetime(2024, 5, 21, 9, 0, 0), 
            closed_at=datetime(2024, 5, 21, 9, 0, 0)),
        OpportunityDto(
            id=5,
            name='Opportunity 5', 
            amount='12', 
            user=list_of_users[4], 
            contact=list_of_contacts[4], 
            status=list_of_statuses[4], 
            opened_at=datetime(2024, 5, 21, 9, 0, 0), 
            closed_at=datetime(2024, 5, 21, 9, 0, 0)),
]

list_of_tasks = []

async def get_contacts():
    return list_of_contacts

async def get_users():
    return list_of_users

async def get_opportunities():
    return list_of_opportunities

async def get_tasks():
    return list_of_tasks