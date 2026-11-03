from fastapi import APIRouter, HTTPException, status

from app.providers.ollama import OllamaProvider
from app.utils.dependencies import PromptsDep
from db.models.ra import RA
from db.models.queries import BasicQuery

controller = APIRouter(prefix="/ra")


@controller.post("/", response_model=RA, status_code=201)
def get_ra(query: BasicQuery, prompts: PromptsDep) -> RA:
    llm = OllamaProvider(sys_prompt=prompts.RA)
    res = llm.get_ra(prompt=query.query)
    if res is None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return res


@controller.post("/batch", response_model=list[RA], status_code=201)
def ra_batch(count: int, prompts: PromptsDep) -> list[RA]:
    if count > 10:
        count = 10
        print("Warning: max count is 10.")
    try:
        llm = OllamaProvider(sys_prompt=prompts.RA)
        user_prompt = "Create an RA item."
        results: list[RA] = []
        while len(results) < count:
            print(f"Creating item {len(results) + 1} of {count}.")
            ra_item: RA = llm.get_ra(prompt=user_prompt)
            results.append(ra_item)
        return results
    except Exception as e:
        print(e)
        raise HTTPException(
            detail="An error occured when creating the RA batch.",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
