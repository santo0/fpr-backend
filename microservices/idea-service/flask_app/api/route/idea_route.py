from flask import Blueprint
from ..model.idea import Idea
from flask import request, jsonify
from db import db


idea_api = Blueprint('idea_api', __name__)


@idea_api.route('/idea/<idea_id>', methods=['GET'])
def get_idea(idea_id):
    # read database
    # notify user logging service via event/message broker
    raise NotImplementedError()


@idea_api.route('/idea', methods=['POST'])
def create_idea():
    print('HOLAAA')
    data = request.json
    name = data['name']
    summary = data['summary']
    description = data['description']
    image_uri = data['image_uri']
    idea = Idea(name=name, summary=summary, description=description, image_uri=image_uri)
    db.session.add(idea)
    db.session.commit()
    # write database
    # notify user service
    # notify search service
    return jsonify(ideaId=idea.id, ideaName=idea.name, status="Created")


@idea_api.route('/idea/<idea_id>', methods=['PUT'])
def edit_idea(idea_id):
    # write database
    # notify user service
    # notify search service
    raise NotImplementedError()


@idea_api.route('/idea/<idea_id>', methods=['DELETE'])
def delete_idea(idea_id):
    # write database
    # notify user service
    # notify search service
    # notify feed service
    raise NotImplementedError()


@idea_api.route('/idea/<idea_id>/follow', methods=['PUT'])
def follow_idea(idea_id):
    # write database
    # notify user service
    # notify user logging service
    # notify feed service
    # notify notification service
    raise NotImplementedError()


@idea_api.route('/idea/<idea_id>/unfollow', methods=['DELETE'])
def unfollow_idea(idea_id):
    # write database
    # notify user service
    # notify feed service
    # notify user logging service
    raise NotImplementedError()
