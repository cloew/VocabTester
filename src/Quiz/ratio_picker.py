import random

class RatioPicker:
    """ Picks elements based on a ratio """
    
    def __init__(self, ratios):
        """ Initialize the Ratio Picker """
        self.ratios = ratios
        
    def getNumberOfResults(self, percentage, total):
        """ Return the number of results for the given percentage """
        num = percentage*total
        leftoverPercentage = num - int(num)
        
        if random.random() < leftoverPercentage:
            numberOfResults = int(num) + 1
        else:
            numberOfResults = int(num)
        
        leftoverPercentage = percentage - float(numberOfResults)/total
        return numberOfResults, leftoverPercentage
        
    def getResults(self, total):
        """ Returns results based on the ratios to get the given number of total results """
        results = []
        leftoverPercentage = 0
        
        for result, percentage in self.ratios:
            numberOfResults, leftoverPercentage = self.getNumberOfResults(percentage+leftoverPercentage, total)
            results += [result]*numberOfResults
        return results