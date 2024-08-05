from pydantic import BaseModel, UUID4


class CompanyBase(BaseModel):
    name: str
    country: str
    meta: dict


class CompanyCreate(CompanyBase):
    name: str
    country: str
    meta: dict


class Company(CompanyBase):
    id: UUID4

    class ConfigDict:
        from_attributes = True
