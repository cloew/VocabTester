import random

def sample_at_most(entries, max):
    """ Sample at most the max number otherwise sample all the entries """
    return random.sample(entries, getNumberToSample(entries, max))

def getNumberToSample(entries, max):
        return min(len(entries), max)