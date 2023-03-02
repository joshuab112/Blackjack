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

    # Function that "hits", or adds a card to, a player's hand.
    # The value of the hand is updated accordingly.
    def hit(self, card):
        self._cards.append(card)

        # If the card dealt is an Ace
        if (card._rank == "A"):

            while (True):

                # The player must choose whether to count the Ace as a 1 or 11
                optionalScore = int(input("Do you want to count the Ace as 1 or 11? "))

                # If the player enters any number besides 1 or 11
                if (optionalScore != 1 and optionalScore != 11):

                    # Prompt the player for valid input
                    print("Ace can only count as 1 or 11!")

                else:

                    # Player has chosen a valid score value
                    print(str(optionalScore) + " it is!")

                    # Add the chosen score to the hand's score value
                    self._score += optionalScore

                    break

        else: 
            self._score += Card.values[card._rank]

    # Function that shows a player's current hand of cards
    # and the score value of said hand. 
    def __str__(self):
        
        if (len(self._cards) > 0):
            currentHand = self._cards[0].__str__()

            for x in range(1, len(self._cards)):
                currentHand += "\n" + self._cards[x].__str__()

            currentHandAndScore = currentHand + "\n" + str(self._score)
        
            return currentHandAndScore

        return "Empty Hand"





