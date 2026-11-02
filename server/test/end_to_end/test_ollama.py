from app.main import app
from app.controllers.ollama_controller import BasicQuery, BasicAnswer
from fastapi.testclient import TestClient

client = TestClient(app)


class TestOllama:
    query_content = BasicQuery(question="Which is bigger, Jupiter or Saturn?")
    base_url = "/ollama/"

    def test_resp_status(self):
        res = client.post(self.base_url, json=self.query_content.model_dump())
        assert res.status_code == 200

    def test_basic_response(self):
        res = client.post(self.base_url, json=self.query_content.model_dump())
        BasicAnswer.model_validate(res.json())
