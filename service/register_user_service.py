import re

from client.users_client import UsersClient
from domain.response import Response
from helpers.constants import ErrorMessages, StatusEnum
from helpers.logger import logger


class RegisterUserService:
    def __init__(self):
        self.email_regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        self.password_regex = re.compile(r'[A-Za-z0-9@#$%^&+=]{8,}')
        self.users_client = UsersClient()

    def validate_input(self, register_user_info):
        if not re.fullmatch(self.email_regex, register_user_info.email):
            logger.error(ErrorMessages.EMAIL_VALIDATION_FAIL)
            return Response(StatusEnum.ERROR, ErrorMessages.EMAIL_VALIDATION_FAIL)
        if not re.fullmatch(self.password_regex, register_user_info.password):
            logger.error(ErrorMessages.PASSWORD_VALIDATION_FAIL)
            return Response(StatusEnum.ERROR, ErrorMessages.PASSWORD_VALIDATION_FAIL)
        message = 'Email and password validation passed'
        logger.info(message)
        return Response(StatusEnum.SUCCESS, message)

    def check_if_user_exists(self, user_data):
        users_response = self.users_client.get_user(user_data.email)
        if users_response.status_code >= 500:
            # Handle users api unavailable
            message = 'An error occurred while sending request to Users.'
            logger.error(message)
            return Response(StatusEnum.INTERNAL_ERROR, message)
        if users_response.status_code == 200:
            # User already registered
            message = 'Sorry. User email already taken. Please use a different one'
            logger.info(message)
            return Response(StatusEnum.ERROR, message)

        # Happy path
        return Response(StatusEnum.SUCCESS, 'User not found in Users.')
