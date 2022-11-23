from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..models.Company import Company
from ..utils.db import get_db

router = APIRouter()


@router.get("/companies")
async def get_companies(db: Session = Depends(get_db), pageNumber: int = 0, pageSize: int = 10):
    return db.query(Company).slice(pageSize * pageNumber, pageSize * pageNumber + pageSize).all()


@router.get("/company/{id}/deals")
async def get_companies(id: int, db: Session = Depends(get_db)):
    return db.query(Company).filter(Company.company_id == id).one().deals
