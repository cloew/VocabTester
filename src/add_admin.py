from Data.language import Language
from Data.user import User
from Server import server

import json
import sys

def addAdminUser(**kwargs):
    """ Add the admin user """
    if 'native_language_id' not in kwargs:
        kwargs['nativeLanguage'] = Language.query.filter_by(name='English').first()
    user = User(is_admin=True, **kwargs)
    server.db.session.add(user)
    server.db.session.commit()

def main(args):
    """ Run the main file """
    input = raw_input()
    print(input)
    with server.app.app_context():
        addAdminUser(**json.loads(input))

if __name__ == "__main__":
    main(sys.argv[1:])