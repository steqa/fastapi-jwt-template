from sqlalchemy import Column, String, text
from sqlalchemy.dialects.postgresql import UUID, BYTEA

from api.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()")
    )
    username = Column(String(255), nullable=False, unique=True)
    password = Column(BYTEA, nullable=False)
