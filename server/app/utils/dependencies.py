from typing import Annotated

from fastapi import Depends
from sqlmodel import Session

from db.engine import get_session
from app.repositories.cat_repository import CatRepository
from app.services.cat_service import CatService


def get_cat_repo(session: Session = Depends(get_session)) -> CatRepository:
    return CatRepository(session=session)


def get_cat_service(repo: CatRepository = Depends(get_cat_repo)) -> CatService:
    return CatService(repo=repo)


CatServiceDep = Annotated[CatService, Depends(get_cat_service)]
