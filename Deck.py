import Card
import random 

'''
Class that represents a deck of cards. 
Each deck will be initalized by creating a 
list of "Card" objects. This list will then be
shuffled so as to make the game fair.
'''
class Deck(object):
    
    def __init__(self):

        # List that will represent a deck of cards.
        # Will consist of "Card" objects.
        self._deck = []

        # Creating a non-shuffled deck of cards
        for suit in range(len(Card.suits)):
            for value in range(len(Card.values)):
                self._deck.append(Card(suit, value))
                print(Card(suit, value))

        # Shuffling the deck of cards
        self.shuffle_deck()

    
    # Function that pops the top card off the deck 
    def deal_card(self):
        return self._deck.pop()

    # Function that shuffles the deck of cards 
    def shuffle_deck(self):
        random.shuffle(self._deck)





