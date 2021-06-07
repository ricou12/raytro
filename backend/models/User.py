from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    email: str
    encrypted_password: str
    is_admin: str
    access_token: str or None
