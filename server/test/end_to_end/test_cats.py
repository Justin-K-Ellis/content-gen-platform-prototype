from fastapi.testclient import TestClient


class TestGetCats:
    def test_returns_200(self, client: TestClient):
        res = client.get("/cats/")
        assert res.status_code == 200

    def test_returns_empty_list_when_no_cats(self, client: TestClient):
        res = client.get("/cats/")
        assert res.json() == []

    def test_returns_cats_after_creation(self, client: TestClient):
        client.post("/cats/", json={"name": "Mouchan", "color": "black"})
        res = client.get("/cats/")
        assert len(res.json()) == 1
        assert res.json()[0]["name"] == "Mouchan"


class TestCreateCat:
    def test_returns_201(self, client: TestClient):
        res = client.post("/cats/", json={"name": "Mouchan", "color": "black"})
        assert res.status_code == 201

    def test_returns_created_cat(self, client: TestClient):
        res = client.post("/cats/", json={"name": "Mouchan", "color": "black"})
        body = res.json()
        assert body["name"] == "Mouchan"
        assert body["color"] == "black"
        assert "public_id" in body

    def test_rejects_missing_fields(self, client: TestClient):
        res = client.post("/cats/", json={"name": "Mouchan"})
        assert res.status_code == 422

    def test_rejects_duplicates(self, client: TestClient):
        url = "/cats/"
        client.post(url, json={"name": "Stella", "color": "gray"})
        res = client.post(url, json={"name": "Stella", "color": "gray"})
        assert res.status_code == 422
