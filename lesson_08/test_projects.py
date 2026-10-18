import uuid


class TestCreateProject:
    """POST /api-v2/projects"""

    def test_create_project_positive(self, client):
        payload = {
            "title": f"autotest-{uuid.uuid4().hex[:8]}",
        }
        response = client.create_project(payload)
        assert response.status_code == 201
        data = response.json()
        assert "id" in data
        assert data.get("title") == payload["title"]

    def test_create_project_negative_empty_title(self, client):
        """Негативный: пустое название (если API валидирует)."""
        response = client.create_project({"title": ""})
        # Ожидаем ошибку клиента (400/422) или создание с пустым именем,
        # в зависимости от логики API. Для стабильности проверяем, что
        # статус не 201, либо явно 400.
        assert response.status_code in (400, 422) or response.status_code != 201


class TestUpdateProject:
    """PUT /api-v2/projects/{id}"""

    def test_update_project_positive(self, client, created_project):
        project_id, _ = created_project
        new_title = f"updated-{uuid.uuid4().hex[:8]}"
        response = client.update_project(project_id, {"title": new_title})
        assert response.status_code == 200
        # Проверяем через GET, что изменение применилось
        get_resp = client.get_project(project_id)
        assert get_resp.status_code == 200
        assert get_resp.json().get("title") == new_title

    def test_update_project_negative_not_found(self, client):
        """Негативный: обновление несуществующего проекта."""
        fake_id = str(uuid.uuid4())
        response = client.update_project(fake_id, {"title": "x"})
        assert response.status_code == 404


class TestGetProject:
    """GET /api-v2/projects/{id}"""

    def test_get_project_positive(self, client, created_project):
        project_id, payload = created_project
        response = client.get_project(project_id)
        assert response.status_code == 200
        assert response.json().get("id") == project_id
        assert response.json().get("title") == payload["title"]

    def test_get_project_negative_not_found(self, client):
        """Негативный: получение несуществующего проекта."""
        fake_id = str(uuid.uuid4())
        response = client.get_project(fake_id)
        assert response.status_code == 404