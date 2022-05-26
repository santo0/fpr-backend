from db import db
from ..models import Idea
from ..interfaces import IdeaInterface


class IdeaService:
    @staticmethod
    def get_by_id(id: int) -> IdeaInterface:
        return Idea.query.filter_by(id=id).first()
