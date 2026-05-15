from app.config.database import database
from uuid import uuid4

task_collection = database["tasks"]


async def create_task(data: dict):
    total_tasks = await task_collection.count_documents({})
    task = {
        "id": f"TASK{total_tasks + 1:03}",
        **data
        }
    
    result = await task_collection.insert_one(task)

    task["_id"] = str(result.inserted_id)

    return task


async def get_task(task_id: str):

    task = await task_collection.find_one(
        {"id": task_id}
    )

    if task:
        task["_id"] = str(task["_id"])

    return task


async def update_task_status(task_id: str, status: str):

    await task_collection.update_one(
        {"id": task_id},
        {"$set": {"status": status}}
    )

    updated_task = await get_task(task_id)

    return updated_task