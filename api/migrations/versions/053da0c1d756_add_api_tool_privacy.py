"""add api tool privacy

Revision ID: 053da0c1d756
Revises: 4829e54d2fee
Create Date: 2024-01-12 06:47:21.656262

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '053da0c1d756'
down_revision = '4829e54d2fee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tool_conversation_variables',
    sa.Column('id', postgresql.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('user_id', postgresql.UUID(), nullable=False),
    sa.Column('tenant_id', postgresql.UUID(), nullable=False),
    sa.Column('conversation_id', postgresql.UUID(), nullable=False),
    sa.Column('variables_str', sa.Text(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP(0)'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP(0)'), nullable=False),
    sa.PrimaryKeyConstraint('id', name='tool_conversation_variables_pkey')
    )
    with op.batch_alter_table('tool_api_providers', schema=None) as batch_op:
        batch_op.add_column(sa.Column('privacy_policy', sa.String(length=255), nullable=True))
        batch_op.alter_column('icon',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.String(length=255),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tool_api_providers', schema=None) as batch_op:
        batch_op.alter_column('icon',
               existing_type=sa.String(length=255),
               type_=sa.VARCHAR(length=256),
               existing_nullable=False)
        batch_op.drop_column('privacy_policy')

    op.drop_table('tool_conversation_variables')
    # ### end Alembic commands ###