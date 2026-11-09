from fastapi import APIRouter, HTTPException, status

from app.providers.ollama import OllamaProvider
from app.utils.dependencies import PromptsDep, RAServiceDep
from db.models.ra import RA, RACreate, RAPublic
from db.models.queries import BasicQuery

controller = APIRouter(prefix="/ra")


@controller.get("/", response_model=list[RA])
def get_ra_items(service: RAServiceDep) -> list[RAPublic]:
    """Return every persisted RA item."""
    return service.index()


@controller.post("/", response_model=RA, status_code=201)
def generate_ra(
    service: RAServiceDep, query: BasicQuery, prompts: PromptsDep
) -> RACreate:
    try:
        return service.gen_ra(sys_prompt=prompts.RA, user_prompt=query.query)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


@controller.post("/batch", response_model=list[RA], status_code=201)
def ra_batch(count: int, prompts: PromptsDep, service: RAServiceDep) -> list[RACreate]:
    try:
        return service.gen_batch(count=count, sys_prompt=prompts.RA)
    except Exception as e:
        print(e)
        raise HTTPException(
            detail="An error occured when creating the RA batch.",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
