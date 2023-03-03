from deck import Deck
from card import Card
from dealerHand import DealerHand
from playerHand import PlayerHand


'''
Class that will act as the main hub for the blackjack game.
Each game is initialized with a dealer, a player, and a 
shuffled deck of cards.It should be noted that a dealer and 
subsequent players are represented by their respective hand of cards
'''
class Blackjack(object):
    
    def __init__(self):
        self.deck = Deck()
        self.dealer = DealerHand()
        self.player = PlayerHand()

    def play(self):

        print("Welcome to Blackjack!\n")
        print("First, let's deal the cards out...")

        # Dealing out the initial cards to the dealer and player
        self.initial_card_dealing()


    def initial_card_dealing(self):

        # Giving the dealer two cards 
        self.dealer.hit(self.deck.deal_card())
        self.dealer.hit(self.deck.deal_card())

        print()

        # Showing only one of the dealer's cards
        print("Here's the dealers initial hand:\n")
        print(self.dealer.obscured_hand())

        # Adding some space
        print()

        # Giving the player two cards
        self.player.hit(self.deck.deal_card())
        self.player.hit(self.deck.deal_card())

        # Showing the player their cards
        print("Here is your first hand:\n")
        print(self.player)


blackjackGame = Blackjack()
blackjackGame.play()
