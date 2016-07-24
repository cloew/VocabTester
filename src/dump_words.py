from Data import Language, Word
from Language.Japanese import WordData
from Server import server

from kao_flask.ext.sqlalchemy import db

import json
import sys

from kao_json import JsonFactory, AsObj, ViaAttr, ViaFn

jsonFactory = JsonFactory({
    Word:AsObj(old_text=ViaAttr('text'), new_text=ViaFn(lambda obj: ''), data=ViaAttr()),
    WordData:AsObj(readings=ViaAttr())
})

def main(args):
    """ Run the main file """
    with server.app.app_context():
        japanese = Language.query.filter_by(name='Japanese').first()
        words = Word.query.filter_by(language=japanese)
        
        wordsJson = jsonFactory.toJson(words)
        with open(args[0], 'w', encoding='utf-8') as f:
            json.dump(wordsJson, f, ensure_ascii=False, indent=4)
            
if __name__ == "__main__":
    main(sys.argv[1:])