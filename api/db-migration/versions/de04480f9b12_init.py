"""init

Revision ID: de04480f9b12
Revises:
Create Date: 2022-03-31 20:23:13.691082

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel
import sqlmodel.sql.sqltypes

# revision identifiers, used by Alembic.
revision = 'de04480f9b12'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('game',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('result',
    sa.Column('game_id', sa.Integer(), nullable=True),
    sa.Column('choice', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('result', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('is_bot', sa.Boolean(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['game_id'], ['game.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('result')
    op.drop_table('game')
    # ### end Alembic commands ###