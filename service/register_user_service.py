import re

from client.users_client import UsersClient
from helpers.constants import ErrorMessages
from helpers.logger import logger


class RegisterUserService:
    def __init__(self):
        self.email_regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        self.password_regex = re.compile(r'[A-Za-z0-9@#$%^&+=]{8,}')

    def validate_input(self, register_user_info):
        response = {'status': None, 'message': None}
        if not re.fullmatch(self.email_regex, register_user_info.email):
            logger.error(ErrorMessages.EMAIL_VALIDATION_FAIL)
            response['status'] = 'error'
            response['message'] = ErrorMessages.EMAIL_VALIDATION_FAIL
            return response
        if not re.fullmatch(self.password_regex, register_user_info.password):
            logger.error(ErrorMessages.PASSWORD_VALIDATION_FAIL)
            response['status'] = 'error'
            response['message'] = ErrorMessages.PASSWORD_VALIDATION_FAIL
            return response
        message = 'Email and password validation passed'
        logger.info(message)
        response['status'] = 'success'
        response['message'] = message
        return response

    def register_user(self, user_data):
        users_response = UsersClient().get_user(user_data.email)
        if users_response.status_code >= 500:
            # Handle users api unavailable
            logger.error('An error occurred while sending request to Users.')
        if users_response.status_code == 200:
            # User already registered
            logger.info('User email already taken. ')

        # Happy path
        logger.info('')
