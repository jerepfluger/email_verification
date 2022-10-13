from http import HTTPStatus

import requests

from config.config import settings as config_file


class UsersClient:
    def __init__(self):
        self.base_url = config_file.users.url

    def get_user(self, email):
        url = f'{self.base_url}/user?email={email}'
        return requests.get(url)
