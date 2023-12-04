"""Update the zip_code column from int to string in job_seekers and recruiters tables and add new column skills in jobs

Revision ID: 048cca55d55e
Revises: cb0fd500f6c0
Create Date: 2023-12-04 15:20:46.284104

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '048cca55d55e'
down_revision: Union[str, None] = 'cb0fd500f6c0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('job_seekers', 'zip_code', type_=sa.String(
        length=32), existing_nullable=True)
    op.alter_column('recruiters', 'zip_code', type_=sa.String(
        length=32), existing_nullable=True)
    op.add_column('jobs', sa.Column(
        'skills_required', sa.String(length=200), default='No skills needed'))


def downgrade() -> None:
    pass
