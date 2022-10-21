class BadRequestException(Exception):
    def __init__(self, description='Bad Request Exception'):
        super(BadRequestException, self).__init__()
        self.code = 400
        self.name = 'Bad Request'
        self.description = description
