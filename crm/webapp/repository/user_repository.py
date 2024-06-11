from ..models import UserDto

list_of_users = [
        UserDto({ 'id': 1, 'username': 'Test1'}),
        UserDto({ 'id': 2, 'username': 'Test2'}),
        UserDto({ 'id': 3, 'username': 'Test3'}),
]

async def get_users():
    return list_of_users

