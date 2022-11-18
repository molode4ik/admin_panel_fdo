from .config import Request
import requests

api_url = f"http://{Request.host}:{Request.port}/api/"


def admin_auth(send_data: dict):
    req = requests.post(api_url+'admin_auth', data=send_data)
    print(req.json())
