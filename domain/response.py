import json
from typing import NewType, Union

from helpers.constants import StatusEnum

StatusValues = NewType('StatusValues', Union[StatusEnum.SUCCESS, StatusEnum.ERROR, StatusEnum.INTERNAL_ERROR])


class Response:
    def __init__(self, status: StatusValues, message):
        self.status = status
        self.message = message

    def to_json(self):
        return {
            'status': self.status,
            'message': self.message
        }
