from Data import User
from kao_flask.ext.auth import KaoAuth

auth = KaoAuth(User, usernameField='email')