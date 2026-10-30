from fastapi import APIRouter

from app.controllers.cat_controller import controller as cat_controller

router = APIRouter()


@router.get("/")
def root() -> dict[str, str]:
    return {"msg": "hello app"}


router.include_router(cat_controller)
