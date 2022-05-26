from flask import Blueprint

idea_api = Blueprint('idea_api', __name__)


@idea_api.route('/idea/<idea_id>', methods=['GET'])
def get_idea(idea_id):
    raise NotImplementedError()


@idea_api.route('/idea', methods=['POST'])
def create_idea():
    raise NotImplementedError()


@idea_api.route('/idea/<idea_id>', methods=['PUT'])
def edit_idea(idea_id):
    raise NotImplementedError()


@idea_api.route('/idea/<idea_id>', methods=['DELETE'])
def delete_idea(idea_id):
    raise NotImplementedError()
