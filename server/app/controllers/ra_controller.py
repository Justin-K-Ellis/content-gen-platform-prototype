import uuid
from fastapi import APIRouter, HTTPException, status

from app.providers.ollama import OllamaProvider
from app.utils.dependencies import PromptsDep, RAServiceDep
from db.models.ra import RA, RACreate, RAPublic
from db.models.queries import BasicQuery

controller = APIRouter(prefix="/ra")


# == Read ==
# == Read all ==
@controller.get("/", response_model=list[RA])
def get_ra_items(service: RAServiceDep) -> list[RAPublic]:
    """Return every persisted RA item."""
    return service.index()


# == Read by id ==
@controller.get("/{id}", response_model=RAPublic)
def get_by_id(service: RAServiceDep, id: uuid.UUID) -> RAPublic:
    return service.get_by_id(public_id=id)


# == Create ==
# == One item ==
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


# == Batch of items ==
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
