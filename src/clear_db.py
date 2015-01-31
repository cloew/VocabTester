from Data.concept import Concept
from Data.language import Language
from Data.word import Word
from Data.symbol import Symbol
from Data.concept_list import ConceptList, concept_list_concepts
from Data.answer import Answer
from Data.mastery import Mastery
from Data.staleness_period import StalenessPeriod
from Data.user import User, learned_symbols, learned_words

from Server import server

import sys

def main(args):
    """ Run the main file """
    with server.app.app_context():
        for table in [concept_list_concepts, learned_symbols, learned_words]:
            d = table.delete()
            server.db.session.execute(d)
    
        for table in [ConceptList, Answer, Mastery, StalenessPeriod, Word, Symbol, Language, Concept, User]:
            table.query.delete()
        server.db.session.commit()

if __name__ == "__main__":
    main(sys.argv[1:])