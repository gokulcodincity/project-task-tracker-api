from fastapi import APIRouter, HTTPException

from app.schemas.project_schema import ProjectCreate
from app.services.project_service import (
    create_project,
    get_project
)

router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)


@router.post("/")
async def add_project(project: ProjectCreate):

    project_data = project.dict()

    project_data["start_date"] = str(
        project_data["start_date"]
    )

    new_project = await create_project(
        project_data
    )

    return {
        "success": True,
        "message": "Project created successfully",
        "data": new_project
    }


@router.get("/{project_id}")
async def fetch_project(project_id: str):

    project = await get_project(project_id)

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    return {
        "success": True,
        "data": project
    }