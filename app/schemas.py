from pydantic import BaseModel


class CompanyBase(BaseModel):
    name: str
    meta: dict


class CompanyCreate(CompanyBase):
    name: str
    meta: dict


class Company(CompanyBase):
    id: int

    class ConfigDict:
        from_attributes = True
