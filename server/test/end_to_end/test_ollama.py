from app.main import app
from fastapi.testclient import TestClient
from db.models.queries import BasicQuery, BasicAnswer

client = TestClient(app)


class TestOllama:
    query_content = BasicQuery(query="Which is bigger, Jupiter or Saturn?")
    base_url = "/ollama/"

    def test_resp_status(self):
        res = client.post(self.base_url, json=self.query_content.model_dump())
        assert res.status_code == 200

    def test_basic_response(self):
        res = client.post(self.base_url, json=self.query_content.model_dump())
        BasicAnswer.model_validate(res.json())
