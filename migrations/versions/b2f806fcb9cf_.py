"""empty message

Revision ID: b2f806fcb9cf
Revises: 
Create Date: 2019-07-09 19:29:06.994199

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b2f806fcb9cf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('member',
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nickname', sa.String(length=100), nullable=False),
    sa.Column('mobile', sa.String(length=11), nullable=False),
    sa.Column('gender', sa.Integer(), nullable=False),
    sa.Column('avatar', sa.String(length=200), nullable=False),
    sa.Column('salt', sa.String(length=32), nullable=False),
    sa.Column('reg_ip', sa.String(length=100), nullable=False),
    sa.Column('status', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('oauth_member_bind',
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('client_type', sa.String(length=20), nullable=False),
    sa.Column('type', sa.Integer(), nullable=False),
    sa.Column('openid', sa.String(length=80), nullable=False),
    sa.Column('unionid', sa.String(length=100), nullable=False),
    sa.Column('extra', sa.Text(), nullable=False),
    sa.Column('member_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['member_id'], ['member.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('oauth_member_bind')
    op.drop_table('member')
    # ### end Alembic commands ###