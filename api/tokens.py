#!/usr/bin/python3
from flask import jsonify, Blueprint
from models import storage
from api.auth import basic_auth

tokens_bp = Blueprint('tokens', __name__, url_prefix='/api')


@tokens_bp.route('/tokens', methods=['POST'])
@basic_auth.login_required
def get_token():
    """
    The token retrieval route that clients will invoke when they need a token
    """
    token = basic_auth.current_user().get_token()
    storage.save()
    return jsonify({'token': token})
