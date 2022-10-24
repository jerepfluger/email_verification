from config.config import settings as config_file
from domain.mock_requests import MockRequests


class UsersClient:
    def __init__(self):
        self.base_url = config_file.users.host

    def get_user(self, email):
        url = f'{self.base_url}/user?email={email}'
        if email == 'return_500@gmail.com':
            return MockRequests(500)
        if email == 'return_200@gmail.com':
            return MockRequests(200)

        # return requests.get(url)
        return MockRequests(404)
