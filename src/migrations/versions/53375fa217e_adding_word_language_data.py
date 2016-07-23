"""Adding Word Language Data

Revision ID: 53375fa217e
Revises: 5376ec8b48d
Create Date: 2016-07-23 14:55:29.285546

"""

# revision identifiers, used by Alembic.
revision = '53375fa217e'
down_revision = '5376ec8b48d'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('masteries', 'answerRating',
               existing_type=sa.INTEGER(),
               nullable=False,
               existing_server_default=sa.text('0'))
    op.add_column('words', sa.Column('language_data', postgresql.JSON(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('words', 'language_data')
    op.alter_column('masteries', 'answerRating',
               existing_type=sa.INTEGER(),
               nullable=True,
               existing_server_default=sa.text('0'))
    ### end Alembic commands ###
