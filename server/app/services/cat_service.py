from app.repositories.cat_repository import CatRepositoryProtocol
from db.models.cat import CatCreate, CatPublic, Cat


class CatService:
    def __init__(self, repo: CatRepositoryProtocol) -> None:
        self.repo = repo

    def create_cat(self, cat_data: CatCreate) -> CatPublic:
        cat = self.repo.create_cat(cat_data)
        return CatPublic(name=cat.name, color=cat.color, public_id=cat.public_id)

    def get_cats(self) -> list[CatPublic]:
        cats: list[Cat] = self.repo.get_cats()
        cats_public: list[CatPublic] = []
        for cat in cats:
            public_cat = CatPublic(
                name=cat.name, color=cat.color, public_id=cat.public_id
            )
            cats_public.append(public_cat)
        return cats_public
