from sqlmodel import Session
from fastapi import APIRouter, Depends
from app.services.cat_service import CatService
from app.repositories.cat_repository import CatRepository
from db.engine import get_session
from db.models.cat import CatPublic

controller = APIRouter(prefix="/cats")


@controller.get("/", response_model=list[CatPublic])
def get_cats(session: Session = Depends(get_session)) -> list[CatPublic]:
    repo = CatRepository(session=session)
    service = CatService(session=session, repo=repo)
    return service.get_cats()
