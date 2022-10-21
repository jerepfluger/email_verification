import re

from client.users_client import UsersClient
from config.config import settings as config_file
from exceptions.exceptions import BadRequestException
from helpers.constants import ErrorMessages, RedisDefaultExpiryTime
from helpers.logger import logger
from helpers.password_encryptor import password_encryptor
from service.email_service import EmailService
from service.redis_service import RedisService


class RegisterService:
    def __init__(self):
        self.email_regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        self.password_regex = re.compile(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$')
        # FIXME: Should find the way to "inject" this
        self.users_client = UsersClient()
        self.redis_service = RedisService()
        self.email_service = EmailService()

    def register(self, user_info):
        self._validate_input(user_info)
        self._validate_user_not_exists(user_info.email)
        uu_id = self.create_redis_entry(user_info)
        self.email_uuid_to_user(user_info.email, uu_id)

        return uu_id

    def _validate_input(self, register_user_info):
        logger.info('Validating user email and password meet requirements')
        if not re.fullmatch(self.email_regex, register_user_info.email):
            logger.error(ErrorMessages.EMAIL_VALIDATION_FAIL)
            raise BadRequestException(ErrorMessages.EMAIL_VALIDATION_FAIL)
        if not re.fullmatch(self.password_regex, register_user_info.password):
            logger.error(ErrorMessages.PASSWORD_VALIDATION_FAIL)
            raise BadRequestException(ErrorMessages.PASSWORD_VALIDATION_FAIL)
        logger.info('Email and password validation passed')

    def _validate_user_not_exists(self, user_email):
        logger.info('Checking if user already exists in database')
        # FIXME: This should go to a UsersService not to UsersClient
        users_response = self.users_client.get_user(user_email)
        if users_response.status_code >= 500:
            # Handle users api unavailable
            message = 'An error occurred while sending request to Users.'
            logger.error(message)
            raise Exception(message)
        if users_response.status_code == 200:
            # User already registered
            message = 'Sorry. User email already taken. Please use a different one'
            logger.info(message)
            raise BadRequestException(message)

        logger.info('User doesn\'t exists. Validation passed.')

    def create_redis_entry(self, user_info):
        logger.info('Creating redis object to be saved')
        encrypted_password = password_encryptor(user_info.password)
        redis_object = {'email': user_info.email, 'password': encrypted_password}

        uu_id = self.redis_service.save_info(redis_object, expiry=RedisDefaultExpiryTime.TEN_MINUTES)
        logger.info('Successfully saved information into redis')

        return uu_id

    def email_uuid_to_user(self, email, uu_id):
        logger.info('Creating email information to be sent to user')
        return_url = f'http://{config_file.api.host}:{config_file.api.port}/validate?id={uu_id}'
        self.email_service.send_verification_email(email, return_url)

        logger.info('Successfully sent email to user')
        return return_url
