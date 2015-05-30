"""empty message

Revision ID: 58cc8ca0faa2
Revises: 4f66c600764a
Create Date: 2015-01-27 18:09:09.573000

"""

# revision identifiers, used by Alembic.
revision = '58cc8ca0faa2'
down_revision = '4f66c600764a'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('learned_words',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('word_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['word_id'], ['words.id'], )
    )
    op.create_table('learned_symbols',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('symbol_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['symbol_id'], ['symbols.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], )
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('learned_symbols')
    op.drop_table('learned_words')
    ### end Alembic commands ###
