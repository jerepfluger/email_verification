from http import HTTPStatus

from flask import g, jsonify
from flask_expects_json import expects_json

from domain.register_dto import RegisterDto
from helpers.logger import logger
from service.register_user_service import RegisterUserService
from . import routes


@routes.route("/register", methods=["POST"])
@expects_json(RegisterDto.get_schema())
def register():
    # FIXME: This should be named differently. Something like 'create_verification_request'
    logger.info('Received sign up request. Starting to process request')
    register_user_service = RegisterUserService()
    register_user_info = RegisterDto(**g.data)
    validation = register_user_service.validate_input(register_user_info)
    if validation.status != 'success':
        return jsonify(validation.to_json()), HTTPStatus.BAD_REQUEST

    check_user_exists = register_user_service.check_if_user_exists(register_user_info)
    if check_user_exists.status != 'success':
        if check_user_exists.status == 'internal_error':
            http_status = HTTPStatus.INTERNAL_SERVER_ERROR
        else:
            http_status = HTTPStatus.BAD_REQUEST
        return jsonify(check_user_exists.to_json(), http_status)

    logger.info('Proceeding to ')
    return jsonify(g.data), HTTPStatus.OK
