class Response:
    def __init__(self, code, name, description):
        self.code = code
        self.name = name
        self.description = description

    def to_json(self):
        return {
            'code': self.code,
            'name': self.name,
            'description': self.description
        }
