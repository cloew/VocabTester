from Data.concept import Concept
from Data.language import Language
from Data.word import Word
from Data.word_list import WordList
from Data.word_answer import WordAnswer
from Data.word_mastery import WordMastery

from Server import server

import sys

def main(args):
    """ Run the main file """
    with server.app.app_context():
        for table in [WordList, Word, Language, Concept, WordMastery, WordAnswer]:
            records = table.query.all()
            [server.db.session.delete(record) for record in records]
        server.db.session.commit()

if __name__ == "__main__":
    main(sys.argv[1:])