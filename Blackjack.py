from deck import Deck
from hand import Hand
from card import Card

class Blackjack:
    pass

deckOfCards = Deck()
playerHand = Hand()
playerHand.hit(deckOfCards.deal_card())
print(playerHand)


