from werkzeug.exceptions import HTTPException
from flask import Blueprint

routes = Blueprint('routes', __name__)

from .basic_controller import *


@routes.errorhandler(HTTPException)
def exception_handler(ex):
    response = ex.get_response()
    response.data = json.dumps({
        'code': ex.code,
        'name': ex.name,
        'description': ex.description,
    })
    response.content_type = 'application/json'

    return response
