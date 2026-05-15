from fastapi import FastAPI

from app.routes.member_route import router as member_router
from app.routes.project_route import router as project_router
from app.routes.task_route import router as task_router

app = FastAPI(
    title="Project Task Tracker API",
    version="1.0.0"
)

app.include_router(member_router)
app.include_router(project_router)
app.include_router(task_router)


@app.get("/")
async def root():

    return {
        "success": True,
        "message": "Project Task Tracker API Running"
    }