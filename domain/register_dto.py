class RegisterDto:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    @staticmethod
    def get_schema():
        return {
            'type': 'object',
            'properties': {
                'email': {'type': 'string'},
                'password': {'type': 'string'}
            },
            'required': ['email', 'password']
        }
