from fastapi_pagination import Params
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy import select
from sqlalchemy.orm import Session
from app import models
from app import schemas


def get(db: Session, company_id: str):
    return db.query(models.Company).filter(models.Company.id == company_id).first()


def get_by_name(db: Session, country: str, name: str):
    return (
        db.query(models.Company)
        .filter(models.Company.name == name and models.Company.country == country)
        .first()
    )


def list(
    db: Session, search: str | None, country: str | None, pagination_params: Params
):
    query = select(models.Company)
    if search:
        query = query.filter(models.Company.name.op("%>")(search)).order_by(
            models.Company.name.op("<->")(search)
        )

    if country:
        query = query.filter(models.Company.country == country)

    return paginate(db, query, pagination_params)


def create(db: Session, company: schemas.CompanyCreate):
    company = models.Company(**company.model_dump())
    db.add(company)
    db.commit()
    db.refresh(company)
    return company
