"""empty message

Revision ID: b83511bc08a9
Revises: cd35b367b0ec
Create Date: 2019-11-03 09:21:38.198195

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b83511bc08a9'
down_revision = 'cd35b367b0ec'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'patient', type_='foreignkey')
    op.drop_column('patient', 'doctor_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('patient', sa.Column('doctor_id', sa.INTEGER(), nullable=True))
    op.create_foreign_key(None, 'patient', 'doctor', ['doctor_id'], ['id'])
    # ### end Alembic commands ###