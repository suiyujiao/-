"""empty message

Revision ID: 522c7391e31b
Revises: be49fab9cf3c
Create Date: 2019-07-15 14:05:16.957263

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '522c7391e31b'
down_revision = 'be49fab9cf3c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('member_address',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('member_id', sa.Integer(), nullable=False),
    sa.Column('nickname', sa.String(length=20), nullable=False),
    sa.Column('mobile', sa.String(length=11), nullable=False),
    sa.Column('province_id', sa.Integer(), nullable=False),
    sa.Column('province_str', sa.String(length=50), nullable=False),
    sa.Column('city_id', sa.Integer(), nullable=False),
    sa.Column('city_str', sa.String(length=50), nullable=False),
    sa.Column('area_id', sa.Integer(), nullable=False),
    sa.Column('area_str', sa.String(length=50), nullable=False),
    sa.Column('address', sa.String(length=100), nullable=False),
    sa.Column('status', sa.Integer(), nullable=False),
    sa.Column('is_default', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['member_id'], ['member.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('member_address')
    # ### end Alembic commands ###
