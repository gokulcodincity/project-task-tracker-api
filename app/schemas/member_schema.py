from pydantic import BaseModel, EmailStr, Field
from typing import List


class MemberCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    role: str
    email: EmailStr
    city: str
    skills: List[str]
    active: bool = True