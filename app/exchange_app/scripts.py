import requests
from .constants import IP, HOST
from django.contrib.auth.models import User
from passlib.hash import bcrypt


def check_auth(username: str, password: str) -> [bool, int]:
    send_data = {
        'username': username,
        'password': password,
    }
    #req = requests.post(url=(IP+HOST), data=send_data).json()
    req = 1
    if req == 1:
        users = User.objects.values_list('username', flat=True)
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
    return bcrypt.hash(password)