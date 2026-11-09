from fastapi import APIRouter, HTTPException, status

from app.providers.ollama import OllamaProvider
from app.utils.dependencies import PromptsDep, RAServiceDep
from db.models.ra import RA, RACreate, RAPublic
from db.models.queries import BasicQuery

controller = APIRouter(prefix="/ra")


# TODO: Enable this endpoint after the RA repository/service dependency exists.
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
def ra_batch(count: int, prompts: PromptsDep) -> list[RACreate]:
    if count > 10:
        count = 10
        print("Warning: max count is 10.")
    try:
        llm = OllamaProvider(sys_prompt=prompts.RA)
        user_prompt = "Create an RA item."
        results: list[RACreate] = []
        while len(results) < count:
            print(f"Creating item {len(results) + 1} of {count}.")
            ra_item: RACreate = llm.gen_ra(prompt=user_prompt)
            results.append(ra_item)
        return results
    except Exception as e:
        print(e)
        raise HTTPException(
            detail="An error occured when creating the RA batch.",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
