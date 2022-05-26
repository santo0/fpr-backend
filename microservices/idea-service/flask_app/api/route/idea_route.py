from flask import Blueprint

idea_api = Blueprint('idea_api', __name__)


@idea_api.route('/idea/<idea_id>', methods=['GET'])
def get_idea(idea_id):
    # read database
    # notify user logging service via event/message broker
    raise NotImplementedError()


@idea_api.route('/idea', methods=['POST'])
def create_idea():
    # write database
    # notify user service
    # notify search service
    raise NotImplementedError()


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
