from web_app import sample



def test_home_page_loads():

    client = sample.test_client()

    resp = client.get("/")

    assert resp.status_code == 200



def test_add_task_redirects():

    client = sample.test_client()

    resp = client.post("/add", data={"task": "Buy milk"}, follow_redirects=False)

    assert resp.status_code in (302, 303)



def test_delete_task_redirects():

    client = sample.test_client()

    client.post("/add", data={"task": "To delete"}, follow_redirects=False)

    resp = client.get("/delete/0", follow_redirects=False)

    assert resp.status_code in (302, 303)


