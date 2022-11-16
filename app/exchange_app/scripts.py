import requests
from .constants import IP, HOST
from django.contrib.auth.models import User


def check_auth(username: str, password: str) -> [bool, int]:
    send_data = {
        'username': username,
        'password': password,
    }
    #req = requests.post(url=(IP+HOST), data=send_data).json()
    req = 1
    if req == 1:
        users = User.objects.values_list('username', flat=True)
        users2 = User.objects.values_list('password', flat=True)
        if username not in users:
            create_authed_users(username, password)
        return True, 2
    else:
        return False, 0


def create_authed_users(username: str, password: str):
    user = User.objects.create_user(username=username,
                                    password=password)
    user.save()


def hash_password(password: str) -> str:
    return ''.join(str(hash(item for item in list(password))))


def search_users(search_query: str, user_data: list) -> list:
    find_data = []
    for record in user_data:
        some = [item for item in record.values() if search_query in item]
        if len(some) > 0:
            find_data.append(record)
    return find_data
