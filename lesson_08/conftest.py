import os
import uuid

import pytest

from api_client import YougileClient


@pytest.fixture(scope="session")
def token():
    """Токен берётся из переменной окружения YOUGILE_TOKEN."""
    value = os.getenv("YOUGILE_TOKEN")
    if not value:
        pytest.skip("Переменная окружения YOUGILE_TOKEN не задана")
    return value


@pytest.fixture(scope="session")
def base_url():
    return "https://ru.yougile.com/api-v2"


@pytest.fixture(scope="session")
def client(base_url, token):
    return YougileClient(base_url, token)


@pytest.fixture
def created_project(client):
    """Создаёт проект перед тестом и удаляет после (если возможно)."""
    # В Yougile поле title обязательно для создания проекта.
    # Поле users можно не передавать, если не требуется назначать участников.
    payload = {
        "title": f"autotest-{uuid.uuid4().hex[:8]}",
    }
    response = client.create_project(payload)
    assert response.status_code == 201, response.text
    project_id = response.json()["id"]

    yield project_id, payload

    # Мягкое удаление через PUT (если поддерживается) или просто оставляем.
    # В реальном задании можно добавить DELETE, если метод доступен.
    client.update_project(project_id, {"deleted": True})