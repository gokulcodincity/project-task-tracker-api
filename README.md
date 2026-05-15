# Project Task Tracker API

## Overview

Project Task Tracker is a backend API project built using FastAPI and MongoDB. This application helps project teams manage members, projects, and tasks efficiently.

The API supports:

- Team member management
- Project management
- Task assignment and tracking
- Task status updates
- Task filtering
- Project progress tracking
- Member task summaries

This project follows proper backend development practices such as:

- FastAPI framework
- Pydantic validation
- MongoDB database integration
- Modular folder structure
- Environment variables using `.env`
- Error handling using `HTTPException`
- Async APIs
- Clean JSON responses

---

# Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming language |
| FastAPI | API framework |
| MongoDB Atlas | Cloud database |
| Motor | Async MongoDB driver |
| Pydantic | Request validation |
| Uvicorn | ASGI server |
| dotenv | Environment variable management |

---

# Project Folder Structure

```bash
project_task_tracker/
│
├── app/
│   ├── config/
│   │   └── database.py
│   │
│   ├── constants/
│   │   └── __init__.py
│   │
│   ├── models/
│   │   ├── member_model.py
│   │   ├── project_model.py
│   │   └── task_model.py
│   │
│   ├── routes/
│   │   ├── member_route.py
│   │   ├── project_route.py
│   │   └── task_route.py
│   │
│   ├── schemas/
│   │   ├── member_schema.py
│   │   ├── project_schema.py
│   │   └── task_schema.py
│   │
│   ├── services/
│   │   ├── member_service.py
│   │   ├── project_service.py
│   │   └── task_service.py
│   │
│   └── main.py
│
├── .env
├── .gitignore
├── README.md
└── pyproject.toml
```

---

# Features

## Member Features

- Create team members
- Fetch member details by ID
- Store skills using list datatype
- Active/inactive member handling

## Project Features

- Create projects
- Fetch project details by ID
- Store technology stack as list

## Task Features

- Create tasks
- Update task status
- Validate task status
- Prevent assigning tasks to inactive members
- Validate member and project existence
- Filter tasks by status
- Filter tasks by assigned member

## Summary Features

- Project progress summary
- Completion percentage calculation
- Member task summary
- Status-wise task count

---

# Environment Variables

Create `.env` file:

```env
MONGODB_URL
DATABASE_NAME
```

---

# Swagger Documentation

Open browser:

```txt
http://127.0.0.1:8000/docs
```

---

# API Endpoints

# Member APIs

## Create Member

### Endpoint

```http
POST /members/
```

### Sample Request

```json
{
  "name": "Gokul",
  "role": "Backend Developer",
  "email": "gokul@gmail.com",
  "city": "Salem",
  "skills": ["Python", "FastAPI", "MongoDB"],
  "active": true
}
```

---

## Fetch Member By ID

### Endpoint

```http
GET /members/{member_id}
```

### Example

```http
GET /members/MEM001
```

---

# Project APIs

## Create Project

### Endpoint

```http
POST /projects/
```

### Sample Request

```json
{
  "project_name": "Project Task Tracker",
  "client_name": "ABC Company",
  "start_date": "2026-05-15",
  "priority": "high",
  "technology_stack": [
    "FastAPI",
    "MongoDB",
    "Python"
  ]
}
```

---

## Fetch Project By ID

### Endpoint

```http
GET /projects/{project_id}
```

### Example

```http
GET /projects/PROJ001
```

---

# Task APIs

## Create Task

### Endpoint

```http
POST /tasks/
```

### Sample Request

```json
{
  "title": "Create Login API",
  "description": "Develop login endpoint",
  "assigned_member_id": "MEM001",
  "project_id": "PROJ001",
  "due_date": "2026-05-25",
  "status": "open"
}
```

---

## Fetch Task By ID

### Endpoint

```http
GET /tasks/{task_id}
```

---

## Update Task Status

### Endpoint

```http
PUT /tasks/{task_id}/status
```

### Sample Request

```json
{
  "status": "completed"
}
```

---

# Task Filter APIs

## Filter Tasks By Status

### Endpoint

```http
GET /tasks/?status=completed
```

---

## Filter Tasks By Member

### Endpoint

```http
GET /tasks/?member_id=MEM001
```

---

# Summary APIs

## Project Progress Summary

### Endpoint

```http
GET /tasks/project-summary/{project_id}
```

### Sample Response

```json
{
  "success": true,
  "project_id": "PROJ001",
  "total_tasks": 5,
  "completed_tasks": 2,
  "pending_tasks": 3,
  "blocked_tasks": 1,
  "completion_percentage": 40.0
}
```

---

## Member Task Summary

### Endpoint

```http
GET /tasks/member-summary/{member_id}
```

### Sample Response

```json
{
  "success": true,
  "member_id": "MEM001",
  "assigned_tasks": 5,
  "status_summary": {
    "open": 1,
    "in_progress": 2,
    "completed": 1,
    "blocked": 1
  }
}
```

---

# Completion Percentage Formula

Completion percentage is calculated using:

Completion Percentage = (Completed Tasks / Total Tasks) × 100

---

# Error Handling

The application uses FastAPI `HTTPException` for handling errors.

## Example Errors

### Member Not Found

```json
{
  "detail": "Member not found"
}
```

### Invalid Status

```json
{
  "detail": "Invalid task status"
}
```

### Inactive Member

```json
{
  "detail": "Cannot assign task to inactive member"
}
```

---

# Valid Task Status Values

```txt
open
in progress
completed
blocked
```

---

# Testing

All APIs were tested using:

- Swagger UI
- Postman

---

# .gitignore

```gitignore
.venv/
__pycache__/
.env
*.pyc

# Conclusion

This Project Task Tracker API demonstrates backend development concepts using FastAPI and MongoDB.

The project includes:

- CRUD APIs
- Request validation
- MongoDB integration
- Async database operations
- API filtering
- Summary analytics
- Proper project architecture
- Error handling
- Environment variable management
