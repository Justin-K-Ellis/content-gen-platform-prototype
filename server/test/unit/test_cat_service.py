import uuid
from db.models.cat import Cat, CatCreate, CatPublic
from app.services.cat_service import CatService


class FakeCatRepository:
    def __init__(self, cats: list[Cat] | None = None) -> None:
        self._cats = cats or []

    def get_cats(self) -> list[Cat]:
        return self._cats

    def create_cat(self, cat_data: CatCreate) -> Cat:
        cat = Cat(name=cat_data.name, color=cat_data.color, public_id=uuid.uuid4())
        self._cats.append(cat)
        return cat

    def get_by_name(self, name: str) -> Cat | None:
        for cat in self._cats:
            if cat.name == name:
                return cat
        return None


class TestGetCats:
    def test_returns_empty_list(self):
        service = CatService(repo=FakeCatRepository())
        assert service.get_cats() == []

    def test_returns_projected_cats(self):
        cat = Cat(name="Mouchan", color="black", public_id=uuid.uuid4())
        service = CatService(repo=FakeCatRepository([cat]))
        result = service.get_cats()
        assert len(result) == 1
        assert isinstance(result[0], CatPublic)
        assert result[0].name == "Mouchan"
        assert result[0].color == "black"
        assert result[0].public_id == cat.public_id


class TestGetByName:
    def test_get_by_name(self):
        cat = Cat(name="Stella", color="gray", public_id=uuid.uuid4())
        service = CatService(repo=FakeCatRepository([cat]))
        stella = service.get_by_name("Stella")
        assert stella is not None
        assert stella.public_id == cat.public_id
