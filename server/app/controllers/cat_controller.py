from fastapi import APIRouter
from app.utils.dependencies import CatServiceDep
from db.models.cat import CatCreate, CatPublic

controller = APIRouter(prefix="/cats")


@controller.post("/", response_model=CatPublic, status_code=201)
def create_cat(cat_data: CatCreate, service: CatServiceDep) -> CatPublic:
    return service.create_cat(cat_data)


@controller.get("/", response_model=list[CatPublic])
def get_cats(service: CatServiceDep) -> list[CatPublic]:
    return service.get_cats()
