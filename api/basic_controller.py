import json
from http import HTTPStatus

from flask import request
from flask import Response as FlaskResponse

from config.config import settings as config_file
from helpers.logger import logger
from repositories.base_repository import BaseRepository
from . import routes


@routes.route("/path/to/controller", methods=["POST"])
def basic_controller():
    json_data = json.loads(request.data)
    logger.info(f'Logging example {config_file.api.name}')
    BaseRepository().add_record()

    return FlaskResponse(json.dumps(json_data, default=lambda o: o.__dict__), status=HTTPStatus.OK)
