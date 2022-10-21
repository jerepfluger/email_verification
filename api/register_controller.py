from http import HTTPStatus

from flask import g, jsonify
from flask_expects_json import expects_json

from domain.register_dto import RegisterDto
from helpers.logger import logger
from service.register_service import RegisterService
from . import routes


@routes.route("/register", methods=["POST"])
@expects_json(RegisterDto.get_schema())
def register():
    # FIXME: This should be named differently. Something like 'create_verification_request'
    logger.info('Received sign up request. Starting to process request')
    register_user_service = RegisterService()
    user_info = RegisterDto(**g.data)
    register_uuid = register_user_service.register(user_info)

    return jsonify({'uuid': register_uuid}), HTTPStatus.OK
