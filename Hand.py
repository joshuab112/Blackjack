'''
Class that represents a hand of cards.
Each hand of cards has a list of "Card" objects 
associated with it as well as the value of the 
current cards in the hand. 
'''
class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.score = 0 


    # Function that shows a player's current hand of cards
    # and the score value of said hand. 
    def __str__(self):

        # Making the hand more presentable
        currentHand = "--------------------\n"
        
        if (len(self.cards) > 0):
            currentHand += "1) " + self.cards[0].__str__()

            for x in range(1, len(self.cards)):
                currentHand += "\n" + str(x + 1) + ") "+ self.cards[x].__str__()
            
            currentHandAndScore = currentHand + "\n\nScore: " + str(self.score)

            # Making the hand and score more presentable
            currentHandAndScore += "\n--------------------"
        
            return currentHandAndScore

        return "Empty Hand"


    # Function that checks whether a hand has busted
    def has_busted(self):

        # If the hand's score is over 21
        if (self.score > 21):

            # The hand has busted
            return True

        # The hand's score stands at or below 21
        return False





