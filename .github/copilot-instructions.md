# Copilot Instructions for Web App

## Architecture Overview
This is a simple Flask-based to-do list web application with in-memory storage. The app consists of:
- `web_app.py`: Main Flask application with routes for viewing, adding, and deleting tasks
- `templates/index.html`: Jinja2 template rendering the task list
- `static/style.css`: Basic CSS styling
- No database; tasks stored in a global Python list (`tasks = []`)

Key routes:
- `GET /`: Display all tasks using `render_template("index.html", tasks=tasks)`
- `POST /add`: Add task from form data and redirect to `/`
- `GET /delete/<int:task_id>`: Remove task by index and redirect to `/`

## Development Workflows
- **Run locally**: `python web_app.py` (runs on host 0.0.0.0, port 5050)
- **Run tests**: `pytest` (uses Flask's test_client for route testing)
- **Docker build**: `docker build -t web-app .`
- **Docker run**: `docker run -p 5050:5050 web-app`

## Project Conventions
- App instance named `sample` (not `app`)
- Global state: Use `tasks` list for data storage (no persistence)
- Route handlers: Simple functions returning redirects or rendered templates
- Testing: Pytest with `client = sample.test_client()` pattern
- Template variables: Pass data directly as kwargs to `render_template`
- Static files: Served from `/static/` URL path, stored in `static/` directory

## Dependencies & Integration
- Flask for web framework
- pytest for testing
- No external APIs or databases
- Containerized with Python 3.9-slim base image

## Code Patterns
- Form handling: `request.form.get("task")` for POST data
- Task deletion: Use list index for deletion (vulnerable to race conditions)
- Redirects: Always `return redirect("/")` after mutations
- Template loops: `{% for task in tasks %}{{ task }}{% endfor %}` with `loop.index0` for delete links