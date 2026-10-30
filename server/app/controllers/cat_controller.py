from fastapi import APIRouter, HTTPException, status
from app.utils.dependencies import CatServiceDep
from db.models.cat import CatCreate, CatPublic

controller = APIRouter(prefix="/cats")


@controller.post("/", response_model=CatPublic, status_code=201)
def create_cat(cat_data: CatCreate, service: CatServiceDep) -> CatPublic:
    try:
        return service.create_cat(cat_data)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_CONTENT)


@controller.get("/", response_model=list[CatPublic])
def get_cats(service: CatServiceDep) -> list[CatPublic]:
    return service.get_cats()
