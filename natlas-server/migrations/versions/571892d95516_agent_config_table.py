"""agent config table

Revision ID: 571892d95516
Revises: 7d9abd1be32c
Create Date: 2019-02-12 15:56:16.843184

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '571892d95516'
down_revision = '7d9abd1be32c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('agent_config',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('versionDetection', sa.Boolean(), nullable=True),
    sa.Column('osDetection', sa.Boolean(), nullable=True),
    sa.Column('defaultScripts', sa.Boolean(), nullable=True),
    sa.Column('onlyOpens', sa.Boolean(), nullable=True),
    sa.Column('scanTimeout', sa.Integer(), nullable=True),
    sa.Column('webScreenshots', sa.Boolean(), nullable=True),
    sa.Column('vncScreenshots', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('agent_config')
    # ### end Alembic commands ###
