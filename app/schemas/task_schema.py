from pydantic import BaseModel
from datetime import date


class TaskCreate(BaseModel):
    title: str
    description: str
    assigned_member_id: str
    project_id: str
    due_date: date
    status: str


class TaskStatusUpdate(BaseModel):
    status: str