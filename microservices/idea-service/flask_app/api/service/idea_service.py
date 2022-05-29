from db import db
from message_controller import MsgCtrl
from ..models import Idea


class IdeaService:
    @staticmethod
    def get_by_id(id: int) -> Idea:
        return Idea.query.filter_by(id=id).first()

    @staticmethod
    def create_idea(idea: Idea) -> Idea:
        db.session.add(idea)
        db.session.commit()
        MsgCtrl.publish_idea_creation(idea)
        return idea

    @staticmethod
    def update_idea(idea: Idea) -> Idea:
        db.session.query(Idea).\
            filter(Idea.id == idea.id).\
            update({'name': idea.name,
                    'summary': idea.summary,
                    'description': idea.description,
                    'image_uri': idea.image_uri})
        db.session.commit()
        MsgCtrl.publish_idea_modification(idea)
        return idea

    @staticmethod
    def delete_idea(idea: Idea) -> Idea:
        Idea.query.filter_by(id=idea.id).delete()
        db.session.commit()
        MsgCtrl.publish_idea_deletion(idea)
        return idea
