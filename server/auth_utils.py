import os
from datetime import datetime, timedelta, timezone
from functools import wraps

import jwt
from flask import request, jsonify, g


def _secret():
    return os.environ['SECRET_KEY']


def create_token(user_id, email):
    payload = {
        'sub': user_id,
        'email': email,
        'exp': datetime.now(timezone.utc) + timedelta(hours=24),
    }
    return jwt.encode(payload, _secret(), algorithm='HS256')


def decode_token(token):
    try:
        return jwt.decode(token, _secret(), algorithms=['HS256'])
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
        return None


def require_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get('Authorization', '')
        if not auth_header.startswith('Bearer '):
            return jsonify(error='Non authentifie'), 401
        token = auth_header[7:]
        payload = decode_token(token)
        if not payload:
            return jsonify(error='Non authentifie'), 401
        g.current_user = {'id': payload['sub'], 'email': payload['email']}
        return f(*args, **kwargs)
    return decorated
