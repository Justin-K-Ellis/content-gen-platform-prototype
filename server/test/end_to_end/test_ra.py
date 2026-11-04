from app.main import app
from fastapi.testclient import TestClient
from db.models.queries import BasicQuery
from db.models.ra import RA

client = TestClient(app)


class TestRA:
    def test_get_ra(self):
        query = BasicQuery(query="Give me an RA item.")
        res = client.post("/ra/", json=query.model_dump())
        data = res.json()
        assert res.status_code == 201
        assert isinstance(RA.model_validate(data), RA)
