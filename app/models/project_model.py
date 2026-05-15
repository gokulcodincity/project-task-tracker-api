from beanie import Document
from typing import List
from datetime import date


class Project(Document):

    project_name: str
    client_name: str
    start_date: date
    priority: str
    technology_stack: List[str]

    class Settings:
        name = "projects"