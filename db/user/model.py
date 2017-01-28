from ..core.model import Base
from .table import users_table


class User(Base):
    __table__ = users_table
