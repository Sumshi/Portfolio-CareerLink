"""create columns first_name, middle_name, last_name and email in applications table

Revision ID: 56abccc1bca7
Revises: daf3cc040ba8
Create Date: 2023-12-02 14:29:54.331032

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '56abccc1bca7'
down_revision: Union[str, None] = 'daf3cc040ba8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """ upgrade function for applications table """
    op.add_column('applications', sa.Column(
        'first_name', sa.String(length=128), nullable=False))
    op.add_column('applications', sa.Column(
        'middle_name', sa.String(length=128), nullable=True))
    op.add_column('applications', sa.Column(
        'last_name', sa.String(length=128), nullable=False))
    op.add_column('applications', sa.Column(
        'email', sa.String(length=128), index=True, nullable=False))


def downgrade() -> None:
    pass
