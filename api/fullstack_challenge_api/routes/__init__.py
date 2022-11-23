from fastapi import APIRouter

from . import companies

backend_router = APIRouter()
backend_router.include_router(companies.router, tags=["companies"])
