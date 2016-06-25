"""Adding Ambiguity Groups to Symbols

Revision ID: 5376ec8b48d
Revises: 207492ecf2d
Create Date: 2016-03-27 03:21:07.819812

"""

# revision identifiers, used by Alembic.
revision = '5376ec8b48d'
down_revision = '207492ecf2d'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('ambiguity_groups',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('symbols', sa.Column('ambiguity_group', sa.Integer(), sa.ForeignKey('ambiguity_groups.id', ondelete="SET NULL"), nullable=True))
    op.add_column('symbols', sa.Column('clarification', sa.UnicodeText(), nullable=True))
    op.create_foreign_key(None, 'symbols', 'ambiguity_groups', ['ambiguity_group'], ['id'], ondelete='SET NULL')


def downgrade():
    op.drop_column('symbols', 'clarification')
    op.drop_column('symbols', 'ambiguity_group')
    op.drop_table('ambiguity_groups')
