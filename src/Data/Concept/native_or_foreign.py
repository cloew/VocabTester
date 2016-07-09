from enum import Enum

class NativeOrForeign(Enum):
    """ Helper class to dynamically get the proper Form from a Concpet Pair """
    Foreign = 1
    Native = 2
    
    def __call__(self, pair):
        """ Return the proepr Form from the given Concept Pair """
        if self is NativeOrForeign.Foreign:
            return pair.foreign
        elif self is NativeOrForeign.Native:
            return pair.native