from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..models.Deal import Deal
from ..utils.db import get_db

router = APIRouter()


@router.get("/deals")
async def get_companies(db: Session = Depends(get_db), pageNumber: int = 0, pageSize: int = 10):
    return db.query(Deal).slice(pageSize * pageNumber, pageSize * pageNumber + pageSize).all()


