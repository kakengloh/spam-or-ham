from fastapi import APIRouter
from .detect import router as detect_router

router = APIRouter()

router.include_router(detect_router, prefix='/detect', tags=['detect'])