from time import sleep
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
        sleep(1.5)
        print("First, let's deal the cards out...")
        sleep(1.5)

        # Dealing out the initial cards to the dealer and player
        self.initial_card_dealing()

        # Entering the main game
        while (True):

            # Giving player the choice to hit or stay
            playerChoice = input("\nDo you wish to hit or stay? ")

            # If the player wishes to hit
            if (playerChoice == "hit"):

                print("\nThe dealer will hit you with another card.")

                sleep(1.5)
                
                print ("\nYour new card...", end = " ")

                sleep(2)

                # Hitting the player with another card
                self.player.hit(self.deck.deal_card())

                # Showing the player their new hand
                print(f"\nHere's your new hand:\n")
                sleep(1)
                print(f"{self.player}")

                # If the player's new hand made them bust
                if (self.player.has_busted()):

                    # Announce their defeat
                    print("\nOh no! You've busted!")
                    print("The dealer wins the game. Better luck next time!")

                    break

            elif (playerChoice == "stay"):

                sleep(1)
                print("\nYou have chosen to stay.")
                sleep(1)
                print(f"You have a final score of {self.player._score}")

                break


    def initial_card_dealing(self):

        # Giving the dealer two cards 
        self.dealer.hit(self.deck.deal_card())
        self.dealer.hit(self.deck.deal_card())

        print()

        # Showing only one of the dealer's cards
        print("Here's the dealers initial hand:\n")
        sleep(2)
        print(self.dealer.obscured_hand())

        print()

        print("Your first card...", end = " ")

        sleep(2)

        # Giving the player their first card
        self.player.hit(self.deck.deal_card())

        sleep(1)

        print("Your second card...", end = " ")

        sleep(2)

        # Giving the player their second card
        self.player.hit(self.deck.deal_card())

        sleep(1.5)

        # Showing the player their first hand
        print("\nHere is your first hand:\n")
        sleep(1)
        print(self.player)


blackjackGame = Blackjack()
blackjackGame.play()
