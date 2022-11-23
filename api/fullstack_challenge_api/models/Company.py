from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.orm import declarative_base, relationship

from ..models.Base import Base


class Company(Base):
    __tablename__ = "company"
    company_id = Column(Integer, primary_key=True)
    name = Column(String(80))
    country = Column(String(80))
    founding_date = Column(DateTime(timezone=True))
    description = Column(Text)
    deals=relationship("Deal",back_populates="company")