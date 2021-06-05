"""Add tags tables

Revision ID: 4a132d6de3b6
Revises: 33cd640e1112
Create Date: 2021-06-05 14:37:46.542980

"""

# revision identifiers, used by Alembic.
revision = "4a132d6de3b6"
down_revision = "33cd640e1112"

from alembic import op
import sqlalchemy as sa
from sqlalchemy_utils import UUIDType
from sqlalchemy.dialects import postgresql


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "cves_tags",
        sa.Column("id", UUIDType(binary=False), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("tags", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column("user_id", UUIDType(binary=False), nullable=True),
        sa.Column("cve_id", UUIDType(binary=False), nullable=True),
        sa.ForeignKeyConstraint(
            ["cve_id"],
            ["cves.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_cves_tags_created_at"), "cves_tags", ["created_at"], unique=False
    )
    op.create_index(
        "ix_cves_tags", "cves_tags", ["tags"], unique=False, postgresql_using="gin"
    )
    op.create_table(
        "users_tags",
        sa.Column("id", UUIDType(binary=False), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("color", sa.String(), nullable=False),
        sa.Column("user_id", UUIDType(binary=False), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_users_tags_created_at"), "users_tags", ["created_at"], unique=False
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_users_tags_created_at"), table_name="users_tags")
    op.drop_table("users_tags")
    op.drop_index(op.f("ix_cves_tags_created_at"), table_name="cves_tags")
    op.drop_index(op.f("ix_cves_tags"), table_name="cves_tags")
    op.drop_table("cves_tags")
    # ### end Alembic commands ###
