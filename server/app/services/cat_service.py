from app.repositories.cat_repository import CatRepositoryProtocol
from db.models.cat import CatCreate, CatPublic, Cat


class CatService:
    def __init__(self, repo: CatRepositoryProtocol) -> None:
        self.repo = repo

    def create_cat(self, cat_data: CatCreate) -> CatPublic:
        existent_cat = self.get_by_name(cat_data.name)
        if existent_cat is not None:
            raise ValueError(f"{cat_data.name} already exits.")
        cat = self.repo.create_cat(cat_data)
        return CatPublic(name=cat.name, color=cat.color, public_id=cat.public_id)

    def get_cats(self) -> list[CatPublic]:
        cats: list[Cat] = self.repo.get_cats()
        cats_public: list[CatPublic] = []
        for cat in cats:
            public_cat = self._to_public(cat)
            cats_public.append(public_cat)
        return cats_public

    def get_by_name(self, name: str) -> CatPublic | None:
        cat = self.repo.get_by_name(name)
        if cat is None:
            return None
        return self._to_public(cat)

    def _to_public(self, cat: Cat) -> CatPublic:
        return CatPublic(name=cat.name, color=cat.color, public_id=cat.public_id)
