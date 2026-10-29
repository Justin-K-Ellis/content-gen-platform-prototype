from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


class TestRoot:
    def test_root_status(self):
        response = client.get("/")
        assert response.status_code == 200

    def test_root_content(self):
        response = client.get("/")
        assert response.json() == {"msg": "hello app"}
