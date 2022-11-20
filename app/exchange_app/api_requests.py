from .config import Request
import requests

api_url = f"http://{Request.host}:{Request.port}/api/"


def admin_auth(send_data: dict) -> dict:
    req = requests.post(api_url+'admin_auth', json=send_data)
    return req.json()


def get_admins() -> list:
    req = requests.post(api_url + 'get_admins')
    return req.json()


def get_students() -> list:
    req = requests.post(api_url + 'get_students')
    return req.json()


def get_groups() -> list:
    req = requests.post(api_url + 'get_groups')
    return req.json()


def get_shedule(group_name: str):
    req = requests.post(api_url + '/get_groups/shedule/'+group_name)
    return req.json()


def get_teachers() -> list:
    req = requests.post(api_url + 'get_teachers')
    return req.json()


def update_admin(send_data: dict):
    req = requests.post(api_url + 'update_admin', json=send_data)
    return req.json()


def delete_admin_id(admin_id: int):
    req = requests.post(api_url + 'delete_admin/' + str(admin_id))


def add_admin(send_data: dict):
    req = requests.post(api_url + 'create_admin', json=send_data)
    return req.json()


def create_teacher(send_data: dict):
    req = requests.post(api_url + 'create_teacher', json=send_data)
    return req.json()
