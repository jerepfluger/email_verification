from flask import Blueprint
from werkzeug.exceptions import BadRequest

from domain.response import Response
from exceptions.exceptions import BadRequestException

routes = Blueprint('routes', __name__)

from .basic_controller import *
from .register_controller import *


@routes.errorhandler(BadRequestException)
def bad_request_handler(ex):
    response = Response(ex.code, ex.name, ex.description)

    return jsonify(response.to_json()), HTTPStatus.BAD_REQUEST


@routes.errorhandler(BadRequest)
def exception_handler(ex):
    response = Response(400, 'Bad Request', ex.description.message)

    return jsonify(response.to_json()), HTTPStatus.INTERNAL_SERVER_ERROR


@routes.errorhandler(Exception)
def exception_handler(ex):
    response = Response(500, 'Internal Server Error', str(ex))

    return jsonify(response.to_json()), HTTPStatus.INTERNAL_SERVER_ERROR
