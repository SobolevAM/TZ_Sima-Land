import uuid
from dataclasses import dataclass

@dataclass
class User:
    id_: uuid.UUID
    first_name: str
    last_name: str
    email: str
    password: str
    birthday: str
