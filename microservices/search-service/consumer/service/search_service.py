
class SearchService:

    def __init__(self, es) -> None:
        self.es = es

    def index_idea(self, id, name):
        self.es.index(index='idea',
                      id=id,
                      body={'idea_name': name},
                      request_timeout=10)

    def index_user(self, id, name):
        self.es.index(index='idea',
                      id=id,
                      body={'user_name': name},
                      request_timeout=10)

    def delete_index(self, index, id):
        self.es.delete(index=index,
                       id=id)
