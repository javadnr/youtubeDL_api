from fastapi import APIRouter, Query
from app.services.get_qualies import get_qualities

router = APIRouter()

@router.get("/get-qualities")
def qualities(data: str = Query(..., description="URL to get it's qualities")):
    return get_qualities(data)