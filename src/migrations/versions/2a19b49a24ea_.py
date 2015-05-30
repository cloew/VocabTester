"""empty message

Revision ID: 2a19b49a24ea
Revises: 45a9ecfe5b70
Create Date: 2015-05-16 19:30:32.158000

"""

# revision identifiers, used by Alembic.
revision = '2a19b49a24ea'
down_revision = '45a9ecfe5b70'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('language_enrollments', sa.Column('id', sa.Integer(), nullable=False))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('language_enrollments', 'id')
    ### end Alembic commands ###
