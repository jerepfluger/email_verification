import json
from http import HTTPStatus

from flask import g, jsonify
from flask import Response as FlaskResponse
from flask_expects_json import expects_json

from config.config import settings as config_file
from domain.register_dto import RegisterDto
from helpers.logger import logger
from service.register_user_service import RegisterUserService
from . import routes


@routes.route("/register", methods=["POST"])
@expects_json(RegisterDto.get_schema())
def register():
    logger.info('Received sign up request. Starting to process request')
    register_user_info = RegisterDto(**g.data)
    register_user_response = RegisterUserService().register_user(register_user_info)

    logger.info('Testing')

    return jsonify(g.data), HTTPStatus.OK