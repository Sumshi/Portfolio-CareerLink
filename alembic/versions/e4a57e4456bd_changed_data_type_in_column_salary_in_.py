"""changed data type in Column salary in jobs table

Revision ID: e4a57e4456bd
Revises: aa3c1008995c
Create Date: 2023-12-01 12:53:11.313098

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e4a57e4456bd'
down_revision: Union[str, None] = 'aa3c1008995c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('jobs', 'salary', type_=sa.String(
        length=32), existing_nullable=True)


def downgrade() -> None:
    pass
