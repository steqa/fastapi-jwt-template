from sqlalchemy import Column, String, text
from sqlalchemy.dialects.postgresql import UUID, BYTEA

from api.database import Base
from api.user.schemas import SUser


class User(Base):
    __tablename__ = "users"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()")
    )
    username = Column(String(255), nullable=False, unique=True)
    password = Column(BYTEA, nullable=False)

    def to_schema(self) -> SUser:
        return SUser(
            id=self.id,
            username=self.username,
            password=self.password
        )
