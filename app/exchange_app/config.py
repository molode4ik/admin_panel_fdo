from dataclasses import dataclass
from environs import Env


env = Env()
env.read_env()


@dataclass
class Request:
    host: str = env.str('REQ_HOST')
    port: str = env.str('REQ_PORT')