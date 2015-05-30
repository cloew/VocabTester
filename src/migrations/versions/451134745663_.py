"""empty message

Revision ID: 451134745663
Revises: 23e909d72d18
Create Date: 2014-12-31 01:40:09.043000

"""

# revision identifiers, used by Alembic.
revision = '451134745663'
down_revision = '23e909d72d18'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('word_lists', sa.Column('name', sa.Unicode(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('word_lists', 'name')
    ### end Alembic commands ###
