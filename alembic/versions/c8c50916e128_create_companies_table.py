"""create companies table

Revision ID: c8c50916e128
Revises: 
Create Date: 2024-08-01 21:56:07.369231

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "c8c50916e128"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "companies",
        sa.Column("id", sa.Uuid, primary_key=True),
        sa.Column("name", sa.String(512), nullable=False),
        sa.Column("country", sa.String(2), nullable=False),
        sa.Column("meta", sa.JSON, nullable=True),
    )
    op.create_index(op.f("ix_companies_name"), "companies", ["name"], unique=True)
    op.create_index(op.f("ix_companies_country"), "companies", ["country"])


def downgrade() -> None:
    op.drop_table("companies")
