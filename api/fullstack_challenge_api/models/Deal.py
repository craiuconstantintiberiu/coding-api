from sqlalchemy import Column, Integer, String, DateTime, Text, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

from ..models.Base import Base


class Deal(Base):
    __tablename__ = "deal"
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DateTime(timezone=True))
    funding_amount = Column(Float)
    funding_round = Column(String(80))
    company_id = Column(Integer, ForeignKey("company.company_id"))
    company = relationship("Company", back_populates="deals")