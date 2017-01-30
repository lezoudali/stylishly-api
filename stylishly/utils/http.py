from flask import jsonify
from werkzeug.exceptions import HTTPException


def abort(message, status_code, headers={}):
    response = jsonify({'error': message})
    response.status_code = status_code
    response.headers = {**headers, 'Content-Type': 'application/vnd.api+json'}
    raise HTTPException(description=None, response=response)
