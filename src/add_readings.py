from Data import Word

from Server import server

import json
import sys

def main(args):
    """ Run the main file """
    filename = args[0]
    with server.app.app_context():
        with open(filename, encoding='utf8') as f:
            with open('readings.log', 'wb') as log:
                data = json.load(f)
                for item in data:
                    word = Word.query.filter_by(text=item['old_text']).first()
                    if not word:
                        log.write(bytes('Unable to find: {}\n'.format(item['old_text']), encoding="utf8"))
                    else:
                        word.text = item['new_text']
                        if word.language_data:
                            word.language_data.merge(item['data'])
                        else:
                            word.language_data = item['data']
                            
                        output = "Merged: {} {}\n".format(repr(word.text), repr(word.language_data))
                        log.write(bytes(output, encoding="utf8"))
        server.db.session.commit()

if __name__ == "__main__":
    main(sys.argv[1:])