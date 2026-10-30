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
    base_url = "/cats/"
    basic_cat = {"name": "Mouchan", "color": "black and white"}

    def test_returns_201(self, client: TestClient):
        res = client.post(self.base_url, json=self.basic_cat)
        assert res.status_code == 201

    def test_returns_created_cat(self, client: TestClient):
        res = client.post(self.base_url, json=self.basic_cat)
        body = res.json()
        assert body["name"] == "Mouchan"
        assert body["color"] == "black and white"
        assert "public_id" in body

    def test_rejects_missing_fields(self, client: TestClient):
        res = client.post(self.base_url, json={"name": "Mouchan"})
        assert res.status_code == 422

    def test_rejects_duplicates(self, client: TestClient):
        client.post(self.base_url, json=self.basic_cat)
        res = client.post(self.base_url, json=self.basic_cat)
        assert res.status_code == 422

    def test_gets_by_name(self, client: TestClient):
        res1 = client.post(self.base_url, json=self.basic_cat)
        res2 = client.get(f"{self.base_url}Mouchan")
        body = res2.json()
        assert res1.status_code == 201
        assert res2.status_code == 200
        assert body["name"] == "Mouchan"
