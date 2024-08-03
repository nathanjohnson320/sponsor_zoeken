"""add company name gin index

Revision ID: 71be84d8f851
Revises: c8c50916e128
Create Date: 2024-08-03 10:50:39.949948

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "71be84d8f851"
down_revision: Union[str, None] = "c8c50916e128"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("CREATE EXTENSION IF NOT EXISTS pg_trgm")
    op.execute("CREATE EXTENSION IF NOT EXISTS btree_gin")

    op.create_index(
        op.f("idx_companies_name_gin"),
        "companies",
        [sa.text("name")],
        postgresql_using="gin",
    )


def downgrade() -> None:
    op.drop_index(op.f("idx_companies_name_gin"), table_name="companies")
