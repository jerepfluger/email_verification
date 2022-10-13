from enum import Enum


class ErrorMessages(str, Enum):
    PASSWORD_VALIDATION_FAIL = 'Provided password should contains at least 8 characters, one uppercase, one lowercase and one special character'
    EMAIL_VALIDATION_FAIL = 'Invalid email provided. Make sure you typed a valid email address'
