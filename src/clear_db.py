from Server import server

import contextlib
import sys

def main(args):
    """ Run the main file """
    with server.app.app_context():
        with contextlib.closing(server.db.engine.connect()) as con:
            trans = con.begin()
            for table in reversed(server.db.metadata.sorted_tables):
                con.execute(table.delete())
            trans.commit()

if __name__ == "__main__":
    main(sys.argv[1:])