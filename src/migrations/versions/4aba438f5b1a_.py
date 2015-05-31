"""empty message

Revision ID: 4aba438f5b1a
Revises: 1b5584dcb7e1
Create Date: 2014-12-30 16:16:09.680000

"""

# revision identifiers, used by Alembic.
revision = '4aba438f5b1a'
down_revision = '1b5584dcb7e1'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('languages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('concepts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('word_lists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('native_id', sa.Integer(), nullable=True),
    sa.Column('test_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['native_id'], ['languages.id'], ),
    sa.ForeignKeyConstraint(['test_id'], ['languages.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('word_list_concepts',
    sa.Column('word_list_id', sa.Integer(), nullable=True),
    sa.Column('concept_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['concept_id'], ['concepts.id'], ),
    sa.ForeignKeyConstraint(['word_list_id'], ['word_lists.id'], )
    )
    op.add_column(u'words', sa.Column('concept_id', sa.Integer(), nullable=True))
    op.add_column(u'words', sa.Column('language_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'words', 'languages', ['language_id'], ['id'])
    op.create_foreign_key(None, 'words', 'concepts', ['concept_id'], ['id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'words', type_='foreignkey')
    op.drop_constraint(None, 'words', type_='foreignkey')
    op.drop_column(u'words', 'language_id')
    op.drop_column(u'words', 'concept_id')
    op.drop_table('word_list_concepts')
    op.drop_table('word_lists')
    op.drop_table('concepts')
    op.drop_table('languages')
    ### end Alembic commands ###