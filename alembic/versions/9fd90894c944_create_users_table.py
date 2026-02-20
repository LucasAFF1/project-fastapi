"""create users table

Revision ID: 9fd90894c944
Revises: 
Create Date: 2026-02-18 13:25:22.147626

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9fd90894c944'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users", 
        sa.Column("id", sa.UUID(as_uuid=True), primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column("username",sa.VARCHAR(20), nullable=False, unique=True),
        sa.Column("email",sa.VARCHAR(256), nullable=False, unique=True) ,
        sa.Column("password",sa.TEXT, nullable=False),

        sa.Column("is_active",sa.Boolean, server_default=sa.text("true"), nullable=False),
        sa.Column("is_staff", sa.Boolean, server_default=sa.text("false"), nullable=False)
    )

    op.create_index(
        "ix_users_username", 
        "users",
        ["username"]
    )

    op.create_index(
        "ix_users_email", 
        "users",
        ["email"]
    )

    op.create_index(
        "ix_users_is_active", 
        "users",
        ["is_active"]
    )

    op.create_index(
        "ix_users_is_staff", 
        "users",
        ["is_staff"]
    )


def downgrade() -> None:
    """Downgrade schema."""
    pass
