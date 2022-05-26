

class IdeaInterface:
    def __init__(self, id, name, summary, description, image_uri) -> None:
        self.id = id
        self.name = name
        self.summary = summary
        self.description = description
        self.image_uri = image_uri
