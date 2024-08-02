from pydantic import BaseModel


class CompanyBase(BaseModel):
    name: str


class CompanyCreate(CompanyBase):
    name: str


class Company(CompanyBase):
    id: int

    class ConfigDict:
        from_attributes = True
