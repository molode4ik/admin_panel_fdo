import json
import os
import hashlib
from django.contrib.auth.models import User, Group
from django.core.files.storage import FileSystemStorage
from .api_requests import admin_auth, get_error_requests, get_conf_requests, get_all_academic_debts, get_all_money_debts


def check_auth(username: str, password: str) -> [bool, int]:
    send_data = {
        'login': username,
        'password': hash_password(password),
    }
    req_data = admin_auth(send_data)
    permission = ''
    if req_data != -1:
        permission = req_data['admin_privilege']
        users = User.objects.values_list('username', flat=True)
        if username not in users:
            create_authed_users(username, password, permission.lower())
        return True, permission
    else:
        return False, permission


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
        some = [str(item) for item in record.values()]
        for s in some:
            if search_query in s:
                find_data.append(record)
                break
    return find_data


def search_user(users: list, user_id: int) -> list:
    for user in users:
        if user_id == user.get('student_id'):
            return user


def search_admin(admins: list, admin_id: int) -> dict:
    for admin in admins:
        if admin_id == admin.get('admin_id'):
            return admin


def search_debt(debts: list, debt_id: int, debt_type: str) -> list:
    search_val = 'money_id'
    if debt_type == 'Академические':
        search_val = 'academic_id'
    for debt in debts:
        if debt_id == debt.get(search_val):
            return debt


def create_common_debts(debts: list, debt_type: str):
    result = []
    search_value = 'money'
    if debt_type == 'Академические':
        search_value = 'academic'
    for debt in debts:
        result.append({
            'debt_id': debt[f'{search_value}_id'],
            'delivery_date': debt[f'{search_value}_delivery_date'],
            'student_id': debt[f'{search_value}_student_id'],
        })
    return result


def create_common_debt(debt: dict, debt_type: str):
    if debt_type == 'Академические':
        return {
            'commentary': debt['academic_commentary'],
            'student_id': debt['academic_student_id'],
            'subject': debt['academic_subject'],
            'delivery_date': debt['academic_delivery_date'],
            'debt_id': debt['academic_id']
        }
    return {
            'commentary': debt['money_commentary'],
            'student_id': debt['money_student_id'],
            'subject': debt['money_sum'],
            'delivery_date': debt['money_delivery_date'],
            'debt_id': debt['money_id']
        }


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


def get_data_from_req(reuqest_type: str):
    if reuqest_type.lower() == 'подтверждение':
        return get_conf_requests()
    return get_error_requests()


def get_debts_data(deb_type: str):
    if deb_type.lower() == 'академические':
        return get_all_academic_debts()
    return get_all_money_debts()

