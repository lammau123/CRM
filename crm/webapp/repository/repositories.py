from ..models import ContactDto, OpportunityDto, UserDto, OpportunityStatusDto, TaskDto, TaskTypeDto, TaskStatusDto
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
            user=list_of_users[0].to_dict(), 
            contact=list_of_contacts[0].to_dict(), 
            status=list_of_statuses[0].to_dict(), 
            opened_at=datetime(2024, 5, 21, 9, 0, 0), 
            closed_at=datetime(2024, 5, 21, 9, 0, 0)),
        OpportunityDto(
            id=2,
            name='Opportunity 2', 
            amount='12', 
            user=list_of_users[1].to_dict(), 
            contact=list_of_contacts[1].to_dict(), 
            status=list_of_statuses[1].to_dict(), 
            opened_at=datetime(2024, 5, 21, 9, 0, 0), 
            closed_at=datetime(2024, 5, 21, 9, 0, 0)),
        OpportunityDto(
            id=3,
            name='Opportunity 3', 
            amount='12', 
            user=list_of_users[2].to_dict(), 
            contact=list_of_contacts[2].to_dict(), 
            status=list_of_statuses[2].to_dict(), 
            opened_at=datetime(2024, 5, 21, 9, 0, 0), 
            closed_at=datetime(2024, 5, 21, 9, 0, 0)),
        OpportunityDto(
            id=4,
            name='Opportunity 4', 
            amount='12', 
            user=list_of_users[3].to_dict(), 
            contact=list_of_contacts[3].to_dict(), 
            status=list_of_statuses[3].to_dict(), 
            opened_at=datetime(2024, 5, 21, 9, 0, 0), 
            closed_at=datetime(2024, 5, 21, 9, 0, 0)),
        OpportunityDto(
            id=5,
            name='Opportunity 5', 
            amount='12', 
            user=list_of_users[4].to_dict(), 
            contact=list_of_contacts[4].to_dict(), 
            status=list_of_statuses[4].to_dict(), 
            opened_at=datetime(2024, 5, 21, 9, 0, 0), 
            closed_at=datetime(2024, 5, 21, 9, 0, 0)),
]

list_of_opportunity_status = [
    OpportunityStatusDto(1, 'New'),
    OpportunityStatusDto(2, 'Inprogress'),
    OpportunityStatusDto(3, 'Delay'),
    OpportunityStatusDto(4, 'Cancel'),
    OpportunityStatusDto(5, 'Completed'),
]

list_of_task_type = [
    TaskTypeDto(id=1, name='task type1'),
    TaskTypeDto(id=2, name='task type2'),
    TaskTypeDto(id=3, name='task type3'),
    TaskTypeDto(id=4, name='task type4'),
    TaskTypeDto(id=5, name='task type5'),
]

list_of_task_status = [
    TaskStatusDto(id=1, name='task status1'),
    TaskStatusDto(id=2, name='task status2'),
    TaskStatusDto(id=3, name='task status3'),
    TaskStatusDto(id=4, name='task status4'),
    TaskStatusDto(id=5, name='task status5'),
]

list_of_tasks = [
    TaskDto(id=1, title='task1', opportunity=list_of_opportunities[0].to_dict(), due_date=datetime.now(), type=list_of_task_type[0].to_dict(), status=list_of_task_status[0].to_dict()),
    TaskDto(id=2, title='task2', opportunity=list_of_opportunities[1].to_dict(), due_date=datetime.now(), type=list_of_task_type[1].to_dict(), status=list_of_task_status[1].to_dict()),
    TaskDto(id=3, title='task3', opportunity=list_of_opportunities[2].to_dict(), due_date=datetime.now(), type=list_of_task_type[2].to_dict(), status=list_of_task_status[2].to_dict()),
    TaskDto(id=4, title='task4', opportunity=list_of_opportunities[3].to_dict(), due_date=datetime.now(), type=list_of_task_type[3].to_dict(), status=list_of_task_status[3].to_dict()),
    TaskDto(id=5, title='task5', opportunity=list_of_opportunities[4].to_dict(), due_date=datetime.now(), type=list_of_task_type[4].to_dict(), status=list_of_task_status[4].to_dict()),
]

def get_contacts():
    return list_of_contacts

def get_users():
    return list_of_users

def get_user_by_id(id):
    user_by_id = { user.id: user for user in get_users() }
    return user_by_id[id]

def get_opportunities():
    return list_of_opportunities

def get_tasks():
    return list_of_tasks

def get_task_by_id(id):
    task_by_id = { task.id: task for task in get_tasks() }
    return task_by_id[id]

def get_opportunity_statuses():
    return list_of_opportunity_status

def get_opportunity_status_by_id(id):
    status_by_id = { status.id: status for status in get_opportunity_statuses() }
    return status_by_id[id]

def get_contact_by_id(id):
    contact_by_id = { contact.id: contact for contact in get_contacts() }
    return contact_by_id[id]

def get_opportunity_by_id(id):
    opportunity_by_id = { opportunity.id: opportunity for opportunity in get_opportunities() }
    return opportunity_by_id[id]

def get_task_types():
    return list_of_task_type

def get_task_type_by_id(id):
    type_by_id = { type.id: type for type in get_task_types() }
    return type_by_id[id]

def get_task_statuses():
    return list_of_task_status

def get_task_status_by_id(id):
    status_by_id = { status.id: status for status in get_task_statuses() }
    return status_by_id[id]