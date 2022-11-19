from .config import Request
import requests

api_url = f"http://{Request.host}:{Request.port}/api/"


def admin_auth(send_data: dict) -> dict:
    req = requests.post(api_url+'admin_auth', json=send_data)
    return req.json()


def get_admins() -> list:
    req = requests.post(api_url + 'get_admins')
    return req.json()


def get_students():
    req = requests.post(api_url + 'get_students')
    return req.json()


def get_groups():
    req = requests.post(api_url + 'get_groups')
    return req.json()


def get_shedule(group_name: str):
    req = requests.post(api_url + '/get_groups/shedule/'+group_name)
    return req.json()

