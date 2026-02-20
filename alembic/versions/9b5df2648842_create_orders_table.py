"""create_orders_table

Revision ID: 9b5df2648842
Revises: 9fd90894c944
Create Date: 2026-02-19 16:16:53.099622

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from app.orders.models import Order_Status, Pizza_Size


# revision identifiers, used by Alembic.
revision: str = '9b5df2648842'
down_revision: Union[str, Sequence[str], None] = '9fd90894c944'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "orders", 
        sa.Column("id", sa.UUID(as_uuid=True), server_default=sa.text("gen_random_uuid()"), primary_key=True),
        sa.Column("quantity", sa.Integer, server_default="1", nullable=False),
        sa.Column("order_status",sa.Enum(Order_Status, name="order_status", create_type=False),server_default="pending", nullable=False),
        sa.Column("pizza_size",sa.Enum(Pizza_Size, name="pizza_size", create_type=False), nullable=False),
        sa.Column("flavour",sa.VARCHAR(20), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column("user_id", sa.UUID(as_uuid=True),sa.ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    )
    op.create_index(
        "ix_orders_order_status",
        "orders",
        ["order_status"]
    )


def downgrade() -> None:
    """Downgrade schema."""
    pass
