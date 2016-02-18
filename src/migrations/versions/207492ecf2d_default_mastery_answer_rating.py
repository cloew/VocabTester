"""Default Mastery Answer Rating

Revision ID: 207492ecf2d
Revises: 4617f59ab8f
Create Date: 2016-01-17 22:09:12.869100

"""

# revision identifiers, used by Alembic.
revision = '207492ecf2d'
down_revision = '4617f59ab8f'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Mastery(Base):
    """ Placeholder for the state of the Mastery table that represents the DB schema for this migration """
    __tablename__ = 'masteries'
    
    id = sa.Column(sa.Integer, primary_key=True)
    answerRating = sa.Column(sa.Integer)
    
Session = sessionmaker(bind=op.get_bind())

def upgrade():
    # Update the Mastery to have the default value
    session = Session()
    for mastery in session.query(Mastery):
        if mastery.answerRating is None:
            mastery.answerRating = 0
            session.add(mastery)
    session.commit()
    
    op.alter_column('masteries', 'answerRating', server_default=sa.text('0'), nullable=True)

def downgrade():
    op.alter_column('masteries', 'answerRating', server_default=None, nullable=False)
