"""creating date posted column in jobs table

Revision ID: daf3cc040ba8
Revises: e4a57e4456bd
Create Date: 2023-12-01 18:42:36.761071

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from datetime import date


# revision identifiers, used by Alembic.
revision: str = 'daf3cc040ba8'
down_revision: Union[str, None] = 'e4a57e4456bd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('jobs', sa.Column('date_posted', sa.Date(), nullable=True, default=date.today()))


def downgrade() -> None:
    pass
