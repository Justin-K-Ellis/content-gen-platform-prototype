import uuid
from app.repositories.ra_repository import RARepositoryProtocol
from db.models.ra import RAPublic, RACreate, RA


class RAService:
    def __init__(self, repo: RARepositoryProtocol) -> None:
        self.repo = repo

    def index(self) -> list[RAPublic]:
        return self.repo.get_all()

    def get_by_id(self, public_id: uuid.UUID) -> RAPublic:
        return self.repo.get_by_id(public_id=public_id)

    def save(self, ra: RACreate) -> RA:
        return self.repo.save_ra(ra=ra)
