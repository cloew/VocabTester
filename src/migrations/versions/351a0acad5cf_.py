"""empty message

Revision ID: 351a0acad5cf
Revises: 348b2c672a27
Create Date: 2015-01-14 05:20:52.864000

"""

# revision identifiers, used by Alembic.
revision = '351a0acad5cf'
down_revision = '348b2c672a27'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('masteries',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('word_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['word_id'], ['words.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('answers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('correct', sa.Boolean(), nullable=True),
    sa.Column('createdDate', sa.DateTime(), nullable=True),
    sa.Column('mastery_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['mastery_id'], ['masteries.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table(u'word_answers')
    op.drop_table(u'word_masteries')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table(u'word_masteries',
    sa.Column(u'id', sa.INTEGER(), server_default=sa.text(u"nextval('word_masteries_id_seq'::regclass)"), nullable=False),
    sa.Column(u'word_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint([u'word_id'], [u'words.id'], name=u'word_masteries_word_id_fkey'),
    sa.PrimaryKeyConstraint(u'id', name=u'word_masteries_pkey')
    )
    op.create_table(u'word_answers',
    sa.Column(u'id', sa.INTEGER(), nullable=False),
    sa.Column(u'correct', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column(u'word_mastery_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column(u'createdDate', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint([u'word_mastery_id'], [u'word_masteries.id'], name=u'word_answers_word_mastery_id_fkey'),
    sa.PrimaryKeyConstraint(u'id', name=u'word_answers_pkey')
    )
    op.drop_table('answers')
    op.drop_table('masteries')
    ### end Alembic commands ###
