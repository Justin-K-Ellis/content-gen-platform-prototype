import yaml
from fastapi import APIRouter, HTTPException, status
from app.providers.ollama import OllamaProvider
from db.models.ra import RA
from app.utils.config import config

controller = APIRouter(prefix="/ra")


@controller.post("/", response_model=RA)
def get_ra(prompt: str) -> RA:
    sys_prompts = yaml.safe_load(config.prompt_dir)
    print(sys_prompts)
    ra_prompt = sys_prompts["RA"]
    llm = OllamaProvider(sys_prompt=ra_prompt)
    res = llm.get_ra(prompt=prompt)
    if res is None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return res
