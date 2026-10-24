import os
import uuid
from pathlib import Path

import pytest
from dotenv import load_dotenv

from api_client import YougileClient

# Автоматически загружать .env (в корне проекта или lesson_08)
load_dotenv(Path(__file__).parent / ".env")


@pytest.fixture(scope="session")
def token():
    value = os.getenv("YOUGILE_TOKEN")
    if not value:
        pytest.skip("Не установлена переменная окружения YOUGILE_TOKEN")
    return value


@pytest.fixture(scope="session")
def base_url():
    return "https://ru.yougile.com/api-v2"


@pytest.fixture(scope="session")
def client(base_url, token):
    return YougileClient(base_url, token)


@pytest.fixture
def created_project(client):
    payload = {"title": f"autotest-{uuid.uuid4().hex[:8]}"}
    response = client.create_project(payload)
    assert response.status_code == 201, response.text
    project_id = response.json()["id"]

    yield project_id, payload

    # Попытка очистки, игнорирование ошибок (API может не поддерживать DELETE)
    try:
        client.delete_project(project_id)
    except Exception:
        pass