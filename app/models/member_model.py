from beanie import Document
from typing import List
from pydantic import EmailStr


class Member(Document):

    name: str
    role: str
    email: EmailStr
    city: str
    skills: List[str]
    active_status: bool

    class Settings:
        name = "members"