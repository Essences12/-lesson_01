import requests


class YougileClient:
    def __init__(self, base_url: str, token: str):
        self.base_url = base_url.rstrip("/")
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }

    def create_project(self, payload: dict) -> requests.Response:
        """POST /api-v2/projects"""
        return requests.post(
            f"{self.base_url}/projects",
            json=payload,
            headers=self.headers,
        )

    def update_project(self, project_id: str, payload: dict) -> requests.Response:
        """PUT /api-v2/projects/{id}"""
        return requests.put(
            f"{self.base_url}/projects/{project_id}",
            json=payload,
            headers=self.headers,
        )

    def get_project(self, project_id: str) -> requests.Response:
        """GET /api-v2/projects/{id}"""
        return requests.get(
            f"{self.base_url}/projects/{project_id}",
            headers=self.headers,
        )