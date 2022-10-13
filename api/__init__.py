from werkzeug.exceptions import HTTPException
from flask import Blueprint

routes = Blueprint('routes', __name__)

from .basic_controller import *
<<<<<<< HEAD
from .register_controller import *
=======
>>>>>>> fdbb4e7d4fd657f7b26bf0672d5ac6d4c3a2243b


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
