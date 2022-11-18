import requests
from django.contrib.auth.models import User, Group
from django.core.files.storage import FileSystemStorage
import json
#from .config import Requests
import os

def check_auth(username: str, password: str) -> [bool, int]:
    send_data = {
        'username': username,
        'password': hash_password(password),
    }
   # req = requests.post(url=(Requests.host+Requests.port+))
    #req = requests.post(url=(IP+HOST), data=send_data).json()
    permission = 'admin'
    req = 1
    if req == 1:
        users = User.objects.values_list('username', flat=True)
        users2 = User.objects.values_list('password', flat=True)
        if username not in users:
            create_authed_users(username, password, permission.lower())
        return True, 2
    else:
        return False, 0


def create_authed_users(username: str, password: str, permission: str):
    user = User.objects.create_user(username=username,
                                    password=password)
    user = add_permissions(user, permission)
    user.save()


# Уточнить по поводу хранения пермишина, переписать получше если все ок Group.objects.get_or_create(name=permission)
def add_permissions(user, permission: str) -> User:
    if 'admin' in permission:
        group, created = Group.objects.get_or_create(name="Admin")
    if 'moder' in permission:
        group, created = Group.objects.get_or_create(name="Moderator")
    if 'view' in permission:
        group, created = Group.objects.get_or_create(name="Viewer")
    user.groups.add(group)
    return user


def hash_password(password: str) -> str:
    return ''.join(str(hash(item for item in list(password))))


def search_users(search_query: str, user_data: list) -> list:
    find_data = []
    for record in user_data:
        some = [item for item in record.values() if search_query in item]
        if len(some) > 0:
            find_data.append(record)
    return find_data


def search_user(users: list, user_id: int) -> list:
    for user in users:
        if user_id == user.get('ID'):
            return user


def search_admin(admins: list, admin_id: int) -> dict:
    for admin in admins:
        if admin_id == admin.get('admin_id'):
            return admin


def parse_file(uploaded_file):
    if uploaded_file.name != '':
        if uploaded_file.content_type == 'application/json':
            fs = FileSystemStorage()
            filename = fs.save(uploaded_file.name, uploaded_file)
            with open("media/" + filename, encoding="utf-8") as json_file:
                data = json.load(json_file)
                print(data)
                for row in data:
                    pass
            os.remove("media/" + filename)
            return data

