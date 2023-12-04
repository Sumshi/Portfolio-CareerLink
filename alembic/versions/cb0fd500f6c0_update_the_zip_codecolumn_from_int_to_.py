"""Update the zip_codecolumn from int to string in job_seekers and recruiters tables

Revision ID: cb0fd500f6c0
Revises: 56abccc1bca7
Create Date: 2023-12-04 15:06:45.056407

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cb0fd500f6c0'
down_revision: Union[str, None] = '56abccc1bca7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
