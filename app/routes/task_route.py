from fastapi import APIRouter, HTTPException, Query

from app.schemas.task_schema import (
    TaskCreate,
    TaskStatusUpdate
)

from app.services.task_service import (
    create_task,
    get_task,
    update_task_status,
    task_collection
)

from app.services.member_service import get_member
from app.services.project_service import get_project

from app.constants import TASK_STATUS

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.post("/")
async def add_task(task: TaskCreate):

    if task.status not in TASK_STATUS:
        raise HTTPException(
            status_code=400,
            detail="Invalid task status"
        )

    member = await get_member(
        task.assigned_member_id
    )

    if not member:
        raise HTTPException(
            status_code=404,
            detail="Member not found"
        )

    if member["active"] is False:
        raise HTTPException(
            status_code=400,
            detail="Cannot assign task to inactive member"
        )

    project = await get_project(
        task.project_id
    )

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    task_data = task.dict()

    task_data["due_date"] = str(
        task_data["due_date"]
    )

    new_task = await create_task(
        task_data
    )

    return {
        "success": True,
        "message": "Task created successfully",
        "data": new_task
    }

@router.get("/{task_id}")
async def fetch_task(task_id: str):

    task = await get_task(task_id)

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return {
        "success": True,
        "data": task
    }


@router.put("/{task_id}/status")
async def change_task_status(
    task_id: str,
    payload: TaskStatusUpdate
):

    if payload.status not in TASK_STATUS:
        raise HTTPException(
            status_code=400,
            detail="Invalid status"
        )

    task = await get_task(task_id)

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    updated_task = await update_task_status(
        task_id,
        payload.status
    )

    return {
        "success": True,
        "message": "Task status updated",
        "data": updated_task
    }


@router.get("/")
async def filter_tasks(
    status: str = Query(None),
    member_id: str = Query(None)
):

    query = {}

    if status:
        query["status"] = status

    if member_id:
        query["assigned_member_id"] = member_id

    tasks = await task_collection.find(
        query,
        {"_id": 0}
    ).to_list(length=100)

    return {
        "success": True,
        "count": len(tasks),
        "data": tasks
    }

@router.get("/project-summary/{project_id}")
async def project_summary(project_id: str):

    project = await get_project(project_id)

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    tasks = await task_collection.find(
        {"project_id": project_id},
        {"_id": 0}
    ).to_list(length=100)

    total_tasks = len(tasks)

    completed_tasks = len([
        task for task in tasks
        if task["status"] == "completed"
    ])

    blocked_tasks = len([
        task for task in tasks
        if task["status"] == "blocked"
    ])

    pending_tasks = len([
        task for task in tasks
        if task["status"] != "completed"
    ])

    completion_percentage = 0

    if total_tasks > 0:
        completion_percentage = (
            completed_tasks / total_tasks
        ) * 100

    return {
        "success": True,
        "project_id": project_id,
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "pending_tasks": pending_tasks,
        "blocked_tasks": blocked_tasks,
        "completion_percentage": round(
            completion_percentage,
            2
        )
    }

@router.get("/member-summary/{member_id}")
async def member_summary(member_id: str):

    member = await get_member(member_id)

    if not member:
        raise HTTPException(
            status_code=404,
            detail="Member not found"
        )

    tasks = await task_collection.find(
        {"assigned_member_id": member_id},
        {"_id": 0}
    ).to_list(length=100)

    total_tasks = len(tasks)

    open_tasks = len([
        task for task in tasks
        if task["status"] == "open"
    ])

    in_progress_tasks = len([
        task for task in tasks
        if task["status"] == "in progress"
    ])

    completed_tasks = len([
        task for task in tasks
        if task["status"] == "completed"
    ])

    blocked_tasks = len([
        task for task in tasks
        if task["status"] == "blocked"
    ])

    return {
        "success": True,
        "member_id": member_id,
        "assigned_tasks": total_tasks,
        "status_summary": {
            "open": open_tasks,
            "in_progress": in_progress_tasks,
            "completed": completed_tasks,
            "blocked": blocked_tasks
        }
    }
