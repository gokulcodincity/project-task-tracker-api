from beanie import Document
from datetime import date


class Task(Document):

    title: str
    description: str
    assigned_member_id: str
    project_id: str
    due_date: date
    status: str

    class Settings:
        name = "tasks"