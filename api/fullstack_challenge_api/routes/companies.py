from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..models.Company import Company
from ..utils.db import get_db

router = APIRouter()


@router.get("/companies")
async def get_companies(db: Session = Depends(get_db)):
    return db.query(Company).all()
