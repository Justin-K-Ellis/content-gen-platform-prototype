from functools import lru_cache
from typing import Annotated

from fastapi import Depends
from sqlmodel import Session
import yaml

from app.utils.config import config
from db.engine import get_session
from db.models.prompts import Prompts
from app.repositories.cat_repository import CatRepository
from app.services.cat_service import CatService


def get_cat_repo(session: Session = Depends(get_session)) -> CatRepository:
    return CatRepository(session=session)


def get_cat_service(repo: CatRepository = Depends(get_cat_repo)) -> CatService:
    return CatService(repo=repo)


@lru_cache
def get_prompts() -> Prompts:
    try:
        with open(config.raw_prompts) as f:
            data = yaml.safe_load(f)
        return Prompts(RA=data["RA"])
    except FileNotFoundError as e:
        print(str(e))
        raise FileNotFoundError(f"{config.raw_prompts} could not be found.")
    except Exception as e:
        print(e)
        raise Exception(
            "Unknown error occured when trying to open the raw prompt file."
        )


CatServiceDep = Annotated[CatService, Depends(get_cat_service)]

PromptsDep = Annotated[Prompts, Depends(get_prompts)]
