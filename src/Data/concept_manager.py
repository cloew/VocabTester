from concept import Concept
from word import Word
            
def findTranslation(word, language):
    """ Find the matching translation of the word in the given language """
    return Word.query.filter_by(concept_id=word.concept_id, language_id=language.id).first()
        
def findConceptMatches(concepts, language):
    """ Return the words matching the given concepts """
    conceptIds = [concept.id for concept in concepts]
    return Word.query.filter(Word.concept_id.in_(conceptIds), Word.language_id==language.id).all()