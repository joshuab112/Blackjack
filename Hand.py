import Card

'''
Class that represents a hand of cards.
Each hand of cards has a list of "Card" objects 
associated with it as well as the value of the 
current cards in the hand. 
'''
class Hand(object):
    
    def __init__(self, deck):
        self._cards = []
        self._score = 0 
        self._deck = deck

    # Function that "hits", or adds a card to, a player's hand.
    # The value of the hand is updated accordingly.
    def hit(self, card):
        card = self._deck.deal_card()
        self._score += Card.values[card._rank]





