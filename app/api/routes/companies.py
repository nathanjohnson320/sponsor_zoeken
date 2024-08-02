from app.contexts import companies
from app.core.db import get_db
from app.schemas import CompanyBase
from fastapi import APIRouter, Depends
from fastapi_pagination import Page, Params
from sqlalchemy.orm import Session


router = APIRouter()


@router.get("/")
def get_companies(
    pagination_params: Params = Depends(), db: Session = Depends(get_db)
) -> Page[CompanyBase]:
    return companies.list(db, pagination_params)