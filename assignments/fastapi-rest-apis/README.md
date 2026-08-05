# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to design and build a REST API using FastAPI, including request handling, validation, and CRUD operations.

## 📝 Tasks

### 🛠️	Build Core API Endpoints

#### Description
Create a FastAPI application for a simple task manager. Add endpoints to list tasks and create new tasks.

#### Requirements
Completed program should:

- Create a FastAPI app in `starter-code.py`
- Define a GET endpoint `/tasks` that returns a list of tasks
- Define a POST endpoint `/tasks` that adds a new task
- Return JSON responses for both endpoints


### 🛠️	Add Validation and CRUD Features

#### Description
Enhance your API with input validation and full CRUD support for individual tasks.

#### Requirements
Completed program should:

- Use a Pydantic model to validate incoming task data
- Add GET `/tasks/{task_id}`, PUT `/tasks/{task_id}`, and DELETE `/tasks/{task_id}` endpoints
- Return appropriate HTTP status codes for success and errors (for example, 404 when task is missing)
- Include at least one example request/response in comments or a separate note
