from app.config.database import database

project_collection = database["projects"]


async def create_project(data: dict):

    total_projects = await project_collection.count_documents({})

    project = {
        "id": f"PROJ{total_projects + 1:03}",
        **data
    }

    result = await project_collection.insert_one(project)

    project["_id"] = str(result.inserted_id)

    return project


async def get_project(project_id: str):

    project = await project_collection.find_one(
        {"id": project_id}
    )

    if project:
        project["_id"] = str(project["_id"])

    return project