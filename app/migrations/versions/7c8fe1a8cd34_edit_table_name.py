"""edit table name

Revision ID: 7c8fe1a8cd34
Revises: 49ed1c623726
Create Date: 2024-09-09 15:40:44.868051

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c8fe1a8cd34'
down_revision = '49ed1c623726'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pages', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=250), nullable=True),
    sa.Column('description', sa.String(length=1000), nullable=True),
    sa.Column('cover', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('Books')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Books',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('pages', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('title', sa.VARCHAR(length=250), autoincrement=False, nullable=True),
    sa.Column('description', sa.VARCHAR(length=1000), autoincrement=False, nullable=True),
    sa.Column('cover', sa.VARCHAR(length=250), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='Books_pkey')
    )
    op.drop_table('books')
    # ### end Alembic commands ###
