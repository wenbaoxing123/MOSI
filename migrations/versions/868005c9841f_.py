"""empty message

Revision ID: 868005c9841f
Revises: 2ed03db70748
Create Date: 2022-09-05 01:11:53.766496

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '868005c9841f'
down_revision = '2ed03db70748'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('SusObject', sa.Column('model_idx', sa.String(length=20), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('SusObject', 'model_idx')
    # ### end Alembic commands ###
