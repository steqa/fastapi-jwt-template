from api.repository import SQLAlchemyRepository
from api.user.models import User


class UserRepository(SQLAlchemyRepository):
    model = User
