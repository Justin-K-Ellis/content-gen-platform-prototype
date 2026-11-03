from fastapi import APIRouter, HTTPException, status

from app.providers.ollama import OllamaProvider
from app.utils.get_prompts import get_prompts
from db.models.ra import RA
from db.models.queries import BasicQuery

controller = APIRouter(prefix="/ra")


@controller.post("/", response_model=RA)
def get_ra(query: BasicQuery) -> RA:
    prompts = get_prompts()
    llm = OllamaProvider(sys_prompt=prompts.RA)
    res = llm.get_ra(prompt=query.query)
    if res is None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return res
