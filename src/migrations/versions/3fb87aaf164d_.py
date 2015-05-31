"""empty message

Revision ID: 3fb87aaf164d
Revises: 1be9e74c2d9e
Create Date: 2015-05-28 02:33:03.291000

"""

# revision identifiers, used by Alembic.
revision = '3fb87aaf164d'
down_revision = '1be9e74c2d9e'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('is_admin', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'is_admin')
    ### end Alembic commands ###