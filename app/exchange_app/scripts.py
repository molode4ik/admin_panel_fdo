import requests
from .constants import IP, HOST
from django.contrib.auth.models import User


def check_auth(username: str, password: str) -> bool:
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
        return True
    else:
        return False


def create_authed_users(username: str, password: str):
    user = User.objects.create_user(username=username,
                                    password=password)
    user.save()
