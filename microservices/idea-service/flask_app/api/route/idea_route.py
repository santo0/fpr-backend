from flask import Blueprint
from ..models import Idea
from flask import request, jsonify, abort
from db import db
from ..service.idea_service import IdeaService

idea_api = Blueprint('idea_api', __name__)


@idea_api.route('/idea/<idea_id>', methods=['GET'])
def get_idea(idea_id):
    idea = IdeaService.get_by_id(int(idea_id))
    # read database
    # notify user logging service via event/message broker
    if idea:
        return jsonify(id=idea.id,
                   ownerId=idea.ownerId,
                   name=idea.name,
                   summary=idea.summary,
                   description=idea.description,
                   image_uri=idea.image_uri,
                   category=idea.category)
    else:
        abort(404) 


    # write database
    # notify search service
    # notify feed service
@idea_api.route('/idea', methods=['POST'])
def create_idea():
    data = request.json
    idea = Idea(**data)
    idea = IdeaService.create_idea(idea)

    return jsonify(ideaId=idea.id, ideaName=idea.name, status="Created")


@idea_api.route('/idea/<idea_id>', methods=['PUT'])
def edit_idea(idea_id):
    # write database
    # notify search service
    # notify feed service
    data = request.json
    idea = Idea(id=idea_id, **data)
    idea = IdeaService.update_idea(idea)

    return jsonify(ideaId=idea.id, ideaName=idea.name, status="Updated")


@idea_api.route('/idea/<idea_id>', methods=['DELETE'])
def delete_idea(idea_id):
    # write database
    # notify search service
    # notify feed service
    idea = Idea(id=idea_id)
    idea = IdeaService.delete_idea(idea)

    return jsonify(ideaId=idea.id, status="Deleted")


@idea_api.route('/idea/<idea_id>/follow', methods=['PUT'])
def follow_idea(idea_id):
    # write database
    # notify user logging service
    # notify feed service
    # notify notification service
    raise NotImplementedError()


@idea_api.route('/idea/<idea_id>/unfollow', methods=['DELETE'])
def unfollow_idea(idea_id):
    # write database
    # notify feed service
    # notify user logging service
    raise NotImplementedError()
