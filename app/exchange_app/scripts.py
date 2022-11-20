import json
import os
import hashlib
from django.contrib.auth.models import User, Group
from django.core.files.storage import FileSystemStorage
from .api_requests import admin_auth


def check_auth(username: str, password: str) -> [bool, int]:
    send_data = {
        'login': username,
        'password': hash_password(password),
    }
    req_data = admin_auth(send_data)
    if req_data != -1:
        permission = req_data['admin_privilege']
        users = User.objects.values_list('username', flat=True)
        if username not in users:
            create_authed_users(username, password, permission.lower())
        return True
    else:
        return False


def create_authed_users(username: str, password: str, permission: str):
    user = User.objects.create_user(username=username,
                                    password=password)
    user = add_permissions(user, permission)
    user.save()


# Уточнить по поводу хранения пермишина, переписать получше если все ок Group.objects.get_or_create(name=permission)

def add_permissions(user, permission: str) -> User:
    group, created = Group.objects.get_or_create(name=permission)
    user.groups.add(group)
    return user


def hash_password(password: str) -> str:
    return hashlib.md5(password.encode()).hexdigest()


def search_users(search_query: str, user_data: list) -> list:
    find_data = []
    for record in user_data:
        some = [item for item in record.values()]
        if search_query in list(map(str, some)):
            find_data.append(record)
    return find_data


def search_user(users: list, user_id: int) -> list:
    for user in users:
        if user_id == user.get('student_id'):
            return user


def search_admin(admins: list, admin_id: int) -> dict:
    for admin in admins:
        if admin_id == admin.get('admin_id'):
            return admin


def search_debt(debts: list, debt_id: int) -> list:
    for debt in debts:
        if debt_id == debt.get('academic_id'):
            return debt


def search_teacher(teachers: list, teacher_id: int) -> dict:
    for teacher in teachers:
        if teacher_id == teacher.get('teacher_id'):
            return teacher


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
