"""Add FTS

Revision ID: 418210551acc
Revises: 8aada469669b
Create Date: 2023-12-18 09:41:20.824339

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import text


# revision identifiers, used by Alembic.
revision = '418210551acc'
down_revision = '8aada469669b'
branch_labels = None
depends_on = None


def upgrade():
    conn = op.get_bind()
    sql = text("""CREATE VIRTUAL TABLE article_search USING fts5(title, content, content=article, content_rowid=article_id,tokenize="porter unicode61");""")
    conn.execute(sql)


def downgrade():
    op.drop_table("article_search")
