from app.repositories.cat_repository import CatRepository
from db.models.cat import CatPublic


class CatService:
    def __init__(self, repo: CatRepository) -> None:
        self.repo = repo

    def get_cats(self) -> list[CatPublic]:
        return self.repo.get_cats()
