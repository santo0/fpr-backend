
from elasticsearch import Elasticsearch


class SearchService:
    def __init__(self, es: Elasticsearch) -> None:
        self.es = es

    def get_users_by_keyword(self, keyword):
        raise NotImplementedError()

    def get_ideas_by_keyword(self, keyword):
        return self.es.search(index="idea",
                              body={"query":
                                    {"match":
                                     {"idea_name": keyword}}})
