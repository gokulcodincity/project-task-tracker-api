from pydantic import BaseModel
from typing import List
from datetime import date


class ProjectCreate(BaseModel):
    project_name: str
    client_name: str
    start_date: date
    priority: str
    technology_stack: List[str]