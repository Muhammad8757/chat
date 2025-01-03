from dataclasses import dataclass

@dataclass
class UserDto:
    username: str = None
    email: str = None
    phone: str = None
    password: str = None

@dataclass
class LoginDto:
    username: str = None
    password: str = None
