from .table import users_table
from ..core.model import Base


class User(Base):
    __table__ = users_table

