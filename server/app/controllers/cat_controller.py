from fastapi import APIRouter
from app.utils.dependencies import CatServiceDep
from db.models.cat import CatPublic

controller = APIRouter(prefix="/cats")


@controller.get("/", response_model=list[CatPublic])
def get_cats(service: CatServiceDep) -> list[CatPublic]:
    return service.get_cats()
