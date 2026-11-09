import uuid
from app.repositories.ra_repository import RARepositoryProtocol
from app.providers.ollama import OllamaProvider
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

    def gen_ra(
        self,
        sys_prompt: str,
        user_prompt: str = "Give me an RA passage",
    ) -> RACreate:
        llm = OllamaProvider(sys_prompt=sys_prompt)
        ra = llm.gen_ra(prompt=user_prompt)
        if ra is None:
            raise ValueError("RA is None")
        return ra

    def gen_batch(self, count: int, sys_prompt: str) -> list[RACreate]:
        if count > 10:
            count = 10
            print("Warning: batch count cannot exceed 10. Batch set to 10.")
        llm = OllamaProvider(sys_prompt=sys_prompt)
        results: list[RACreate] = []
        while len(results) < count:
            print(f"Creating item {len(results) + 1} of {count}.")
            ra_item: RACreate = llm.gen_ra(prompt="Create an RA item.")
            results.append(ra_item)
        return results
