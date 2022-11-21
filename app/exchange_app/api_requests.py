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


def update_student(send_data: dict):
    req = requests.post(api_url + 'update_student', json=send_data)
    print(req.json())
    return req.json()


def get_groups() -> list:
    req = requests.post(api_url + 'get_groups')
    return req.json()


def get_shedule(group_name: str):
    req = requests.post(api_url + 'get_groups/shedule/' + group_name)
    return req.json()


def update_shedule():
    req = requests.post(api_url + 'update_shedule')


def get_teachers() -> list:
    req = requests.post(api_url + 'get_teachers')
    return req.json()


def delete_teacher(teacher_id: int):
    req = requests.post(api_url + 'delete_teacher/' + str(teacher_id))
    return req.json()


def update_teacher(send_data: dict):
    req = requests.post(api_url + 'update_teacher', json=send_data)
    return req.json()


def delete_debt(debt_id: int):
    req = requests.post(api_url + 'delete_academic_debts/' + str(debt_id))
    return req.json()


def del_money_debt(money_id: int):
    req = requests.post(api_url + 'delete_money_debts/' + str(money_id))
    return req.json()


def get_all_academic_debts() -> list:
    req = requests.post(api_url + 'get_all_academic_debts')
    return req.json()


def get_all_money_debts() -> list:
    req = requests.post(api_url + 'get_all_money_debts')
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


def get_conf_requests():
    req = requests.post(api_url + 'get_confirmation_requests')
    return req.json()


def get_error_requests():
    req = requests.post(api_url + 'get_error_requests')
    return req.json()


def del_error_request(error_id: int):
    req = requests.post(api_url + 'delete_error_request/' + str(error_id))
    return req.json()


def confirm_req(confirm_id: int):
    req = requests.post(api_url + 'confirm_confirmation_request/' + str(confirm_id))
    return req.json()


def delete_confirm_req(confirm_id: int):
    req = requests.post(api_url + 'delete_confirmation_request/' + str(confirm_id))
    return req.json()
