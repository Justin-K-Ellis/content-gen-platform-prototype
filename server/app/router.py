from fastapi import APIRouter

from app.controllers.cat_controller import controller as cat_controller
from app.controllers.ollama_controller import controller as ollama_controller
from app.controllers.ra_controller import controller as ra_controller

router = APIRouter()


@router.get("/")
def root() -> dict[str, str]:
    return {"msg": "hello app"}


router.include_router(cat_controller)
router.include_router(ollama_controller)
router.include_router(ra_controller)
