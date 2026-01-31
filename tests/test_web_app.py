from web_app import sample, tasks
import pytest



@pytest.fixture(autouse=True)
def reset_tasks():
    """Reset the global tasks list before each test to ensure isolation."""
    global tasks
    tasks.clear()
    yield
    tasks.clear()pytes



def test_home_page_loads():
    client = sample.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"Simple To-Do App" in resp.data  # Check page title



def test_home_page_displays_tasks():
    client = sample.test_client()
    tasks.append("Test task")
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"Test task" in resp.data  # Task appears in HTML



def test_add_task_redirects():
    client = sample.test_client()
    resp = client.post("/add", data={"task": "Buy milk"}, follow_redirects=False)
    assert resp.status_code in (302, 303)
    assert resp.headers["Location"] == "/"  # Redirects to home



def test_add_task_adds_to_list():
    client = sample.test_client()
    client.post("/add", data={"task": "Buy milk"})
    assert "Buy milk" in tasks



def test_add_empty_task_does_not_add():
    client = sample.test_client()
    initial_len = len(tasks)
    client.post("/add", data={"task": ""})
    assert len(tasks) == initial_len  # No task added if empty



def test_delete_task_redirects():
    client = sample.test_client()
    tasks.append("To delete")
    resp = client.get("/delete/0", follow_redirects=False)
    assert resp.status_code in (302, 303)
    assert resp.headers["Location"] == "/"



def test_delete_task_removes_from_list():
    client = sample.test_client()
    tasks.append("Task 1")
    tasks.append("Task 2")
    client.get("/delete/0")
    assert tasks == ["Task 2"]  # First task removed



def test_delete_invalid_id_does_nothing():
    client = sample.test_client()
    tasks.append("Only task")
    client.get("/delete/5")  # Invalid index
    assert tasks == ["Only task"]  # List unchanged


