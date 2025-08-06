"""merge heads

Revision ID: 8956c610aef0
Revises: 285d13267b39, f40ec4d2a035
Create Date: 2025-08-06 16:51:49.131771

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8956c610aef0'
down_revision: Union[str, Sequence[str], None] = ('285d13267b39', 'f40ec4d2a035')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
