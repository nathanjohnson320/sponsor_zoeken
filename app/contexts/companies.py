from fastapi_pagination import Params
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy import select
from sqlalchemy.orm import Session
from app import models


def get(db: Session, company_id: str):
    return db.query(models.Company).filter(models.Company.id == company_id).first()


def get_by_name(db: Session, name: str):
    return db.query(models.Company).filter(models.Company.name == name).first()


def list(db: Session, params: Params):
    return paginate(db, select(models.Company), params)


def create(db: Session, name: str, meta: dict):
    company = models.Company(name=name, meta=meta)
    db.add(company)
    db.commit()
    db.refresh(company)
    return company
