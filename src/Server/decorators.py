import jwt

from functools import wraps
from flask import request, jsonify
from Server.helpers.user_proxy import UserProxy

# Authentication attribute/annotation
def authenticate(error):
  resp = jsonify(error)

  resp.status_code = 401

  return resp

def requires_auth(f):
  @wraps(f)
  def decorated(*args, **kwargs):
    auth = request.headers.get('Authorization', None)
    if not auth:
      return authenticate({'code': 'authorization_header_missing', 'description': 'Authorization header is expected'})

    parts = auth.split()

    if parts[0].lower() != 'bearer':
      return {'code': 'invalid_header', 'description': 'Authorization header must start with Bearer'}
    elif len(parts) == 1:
      return {'code': 'invalid_header', 'description': 'Token not found'}
    elif len(parts) > 2:
      return {'code': 'invalid_header', 'description': 'Authorization header must be Bearer + \s + token'}

    token = parts[1]
    try:
        payload = jwt.decode(token, 'secret token')
        # payload = jwt.decode(
            # token,
            # base64.b64decode(env["AUTH0_CLIENT_SECRET"].replace("_","/").replace("-","+"))
        # )
    # except jwt.ExpiredSignature:
        # return authenticate({'code': 'token_expired', 'description': 'token is expired'})
    except jwt.DecodeError:
        return authenticate({'code': 'token_invalid_signature', 'description': 'token signature is invalid'})

    # if payload['aud'] != env["AUTH0_CLIENT_ID"]:
      # return authenticate({'code': 'invalid_audience', 'description': 'the audience does not match. expected: ' + CLIENT_ID})
      
    kwargs['user'] = UserProxy(payload)
    return f(*args, **kwargs)

  return decorated
  
def requires_admin(f):
  @wraps(f)
  def decorated(*args, **kwargs):
    user = kwargs['user']
    if not user.is_admin:
        return authenticate({'code': 'non_admin_user', 'description': 'User does not have admin privileges'})
    return f(*args, **kwargs)
  return decorated