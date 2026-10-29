from fastapi import APIRouter

from app.controllers.cat_controller import controller as cat_controller

router = APIRouter()
router.include_router(cat_controller)
