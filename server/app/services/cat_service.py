from app.repositories.cat_repository import CatRepository
from db.models.cat import CatPublic, Cat


class CatService:
    def __init__(self, repo: CatRepository) -> None:
        self.repo = repo

    def get_cats(self) -> list[CatPublic]:
        cats: list[Cat] = self.repo.get_cats()
        cats_public: list[CatPublic] = []
        for cat in cats:
            public_cat = CatPublic(
                name=cat.name, color=cat.color, public_id=cat.public_id
            )
            cats_public.append(public_cat)
        return cats_public
