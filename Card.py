''' 
Class that represents a single card. 
Each card contains a suit and a value associated
with said suite.
'''
class Card(object):

    suits = ["Spades", "Hearts", "Diamonds", "Clubs"]

    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "K", "Q", "A"]

    # Dictionary that maps the ranks to their respective numerical values 
    values = {"2": 2, "3" : 3, "4" :4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
              "J": 10, "K": 10, "Q": 10, "A": 11}
    
    def __init__(self, suit, rank):
        self._suit = suit
        self._rank = rank

    # Function that will return the specific value of a card
    def __str__(self):
        return f'{Card.values[self._value]} of {Card.values[self._value]}'




