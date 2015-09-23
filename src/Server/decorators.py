from functools import wraps
from flask import jsonify

# Authentication attribute/annotation
def authenticate(error):
  resp = jsonify(error)
  resp.status_code = 401
  return resp
  
def requires_admin(f):
  @wraps(f)
  def decorated(*args, **kwargs):
    user = kwargs['user']
    if not user.is_admin:
        return authenticate({'code': 'non_admin_user', 'description': 'User does not have admin privileges'})
    return f(*args, **kwargs)
  return decorated