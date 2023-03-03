from card import Card

'''
Class that represents a hand of cards.
Each hand of cards has a list of "Card" objects 
associated with it as well as the value of the 
current cards in the hand. 
'''
class Hand(object):
    
    def __init__(self):
        self._cards = []
        self._score = 0 

    # Function that shows a player's current hand of cards
    # and the score value of said hand. 
    def __str__(self):
        
        if (len(self._cards) > 0):
            currentHand = self._cards[0].__str__()

            for x in range(1, len(self._cards)):
                currentHand += "\n" + self._cards[x].__str__()

            currentHandAndScore = currentHand + "\nScore of " + str(self._score)
        
            return currentHandAndScore

        return "Empty Hand"





