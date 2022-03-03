from typing import Any

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from api import depends

router = APIRouter()

@router.get("/")
def get_posts(
        db: Session = Depends(depends.get_db)
) -> Any:
    Session

    return "123"
