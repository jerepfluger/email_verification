from http import HTTPStatus

from client.users_client import UsersClient
from helpers.logger import logger


class RegisterUserService:
    def __init__(self):
        pass

    def register_user(self, user_data):
        users_response = UsersClient().get_user(user_data.email)
        if users_response.status_code >= 500:
            # Handle users api unavailable
            logger.info('')
        if users_response.status_code == 200:
            # User already registered
            logger.info('')

        # Happy path
