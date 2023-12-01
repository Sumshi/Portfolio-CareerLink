"""created columns open_position and date_posted in jobs table

Revision ID: aa3c1008995c
Revises: 
Create Date: 2023-12-01 11:24:57.356255

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'aa3c1008995c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('jobs', sa.Column('open_position', sa.String(
        length=32), nullable=True, server_default='1'))


def downgrade() -> None:
    pass
