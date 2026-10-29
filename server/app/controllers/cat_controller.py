from fastapi import APIRouter
from app.services import cat_service as service

controller = APIRouter(prefix="/kats")


@controller.get("/", response_model=list[str])
def get_cats() -> list[str]:
    return service.get_cats()
