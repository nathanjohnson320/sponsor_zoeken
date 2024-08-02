from app.core.db import Base
from sqlalchemy import (
    Column,
    String,
)
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column
import uuid


class Company(Base):
    __tablename__ = "companies"

    id: Mapped[str] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    name = Column(String, index=True)
    meta = Column(JSONB)
