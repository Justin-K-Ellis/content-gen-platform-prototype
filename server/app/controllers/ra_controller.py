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


# @controller.post("/{count}", response_model=list[RA])
# ... # TODO
