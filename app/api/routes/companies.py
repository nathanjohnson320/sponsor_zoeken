from app.contexts import companies
from app.core.db import get_db
from app.schemas import Company
from fastapi import APIRouter, Depends
from fastapi_pagination import Page, Params
from sqlalchemy.orm import Session


router = APIRouter()


@router.get("/")
def get_companies(
    search: str | None = None,
    country: str | None = None,
    pagination_params: Params = Depends(),
    db: Session = Depends(get_db),
) -> Page[Company]:
    return companies.list(
        db=db, pagination_params=pagination_params, search=search, country=country
    )
