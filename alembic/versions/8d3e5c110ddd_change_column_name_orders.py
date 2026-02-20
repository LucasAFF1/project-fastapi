"""change_column_name_orders

Revision ID: 8d3e5c110ddd
Revises: 9b5df2648842
Create Date: 2026-02-19 16:33:52.802336

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8d3e5c110ddd'
down_revision: Union[str, Sequence[str], None] = '9b5df2648842'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column("orders", "created_at", new_column_name="ordered_at")


def downgrade() -> None:
    """Downgrade schema."""
    pass
