import uuid


class TestCreateProject:
    def test_create_project_positive(self, client):
        payload = {"title": f"autotest-{uuid.uuid4().hex[:8]}"}
        response = client.create_project(payload)
        assert response.status_code == 201
        project_id = response.json()["id"]

        # Проверка через GET
        get_resp = client.get_project(project_id)
        assert get_resp.status_code == 200
        assert get_resp.json().get("title") == payload["title"]

    def test_create_project_negative_empty_title(self, client):
        response = client.create_project({"title": ""})
        assert response.status_code == 400  # Строгая проверка


class TestUpdateProject:
    def test_update_project_positive(self, client, created_project):
        project_id, _ = created_project
        new_title = f"updated-{uuid.uuid4().hex[:8]}"
        response = client.update_project(project_id, {"title": new_title})
        assert response.status_code == 200

        get_resp = client.get_project(project_id)
        assert get_resp.status_code == 200
        assert get_resp.json().get("title") == new_title

    def test_update_project_negative_not_found(self, client):
        fake_id = str(uuid.uuid4())
        response = client.update_project(fake_id, {"title": "x"})
        assert response.status_code == 404


class TestGetProject:
    def test_get_project_positive(self, client, created_project):
        project_id, payload = created_project
        response = client.get_project(project_id)
        assert response.status_code == 200
        assert response.json().get("id") == project_id
        assert response.json().get("title") == payload["title"]

    def test_get_project_negative_not_found(self, client):
        fake_id = str(uuid.uuid4())
        response = client.get_project(fake_id)
        assert response.status_code == 404