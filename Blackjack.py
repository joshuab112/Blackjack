from time import sleep
from deck import Deck
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

        print("First, let's deal the cards out...\n")

        sleep(1.5)

        # Dealing out the initial cards to the dealer and player
        self.initial_card_dealing()

        sleep(1)

        # Now it's the players turn. This variable will hold the outcome
        # of the player's turn
        playerTurnOutcome = self.player_turn()

        # If the "player_turn" function return "bust", this means the player 
        # busted and has therefore lost the game
        if (playerTurnOutcome == "bust"):

            # Announcing the player's defeat
            print("\nOh no! You've busted!")
            print("The dealer wins the game. Better luck next time!")

        # If the player did not bust and chose to stay
        elif (playerTurnOutcome == "stay"):
            
            sleep(1)

            print("\nYou have chosen to stay.")

            sleep(1)

            print(f"\nYou have a final score of {self.player.score}\n")

            sleep(1)

            # The dealer will now play
            self.dealer_turn()


    def initial_card_dealing(self):

        print("Your first card...", end = " ")

        sleep(1)

        # Giving the player their first card
        self.player.hit(self.deck.deal_card())

        sleep(1)

        print("Dealer's first card...", end = " ")

        sleep(1)

        # Giving the dealer their first card
        self.dealer.hit(self.deck.deal_card())

        # Showing the dealer's first card
        print(f"{self.dealer.cards[0]}\n")

        sleep(1)

        print("Your second card...", end = " ")

        sleep(1)

        # Giving the player their second card
        self.player.hit(self.deck.deal_card())

        sleep(1)

        print("Dealer's second card...", end = " ")

        # Giving the dealer their second card
        self.dealer.hit(self.deck.deal_card())

        sleep(1)

        print("{Hidden}")

        sleep(1)

        # Showing the dealer's initial hand
        print("\nHere is the dealer's initial hand:\n")

        sleep(1.5)

        print(self.dealer.obscured_hand())

        sleep(1.5)

        # Showing the player their initial hand
        print("\nHere is your initial hand:\n")

        sleep(1.5)

        print(self.player)


    # Function that activates the player's turn.
    # Returns "bust" if the player has busted or "stay" if
    # the player chose to stay.
    def player_turn(self):

        while True:

            # Giving player the choice to hit or stay
            playerChoice = input("\nDo you wish to hit or stay? ")

            # If the player chooses to hit
            if (playerChoice.lower() == "hit"):

                sleep(1)

                print("\nThe dealer will hit you with another card.")

                sleep(1)
                
                print ("\nYour new card...", end = " ")

                sleep(1)

                # Hitting the player with another card
                self.player.hit(self.deck.deal_card())

                sleep(1)

                # Showing the player their new hand
                print("Here's your new hand:\n")

                sleep(1)

                print(f"{self.player}")

                sleep(1)

                # If the player's new hand made them bust
                if (self.player.has_busted()):

                    return "bust"             

            # If the player chooses to stay
            elif (playerChoice.lower() == "stay"):

                return "stay"

            else:
                print("\nPlease select a valid choice")


    # Function that activates the dealer's turn.
    # Dealer's final score is compared against player's final score.
    # The result of the game is returned.
    def dealer_turn(self):

        print("Now let's see the dealer's hand...\n")

        sleep(1)

        print(self.dealer)

        sleep(1)

        # Dealer can only stand if their score is higher than 17 but less than 21
        if (self.dealer.score < 17):

            print("Dealer's score is less than 17 so they must hit!\n")

            # Dealer must draw until their score is 17 or above
            while (self.dealer.score < 17):

                sleep(1)

                print("Dealer's new card...", end = " ")

                # Giving the dealer a new card
                self.dealer.hit(self.deck.deal_card())

                # Showing the dealer's first card
                print(f"{self.dealer.cards[-1]}\n")

                sleep(1)

                # If dealer's score is less than 17 after being given new card
                if (self.dealer.score < 17):

                    print(f"Dealer's score of {self.dealer.score} is still less than 17.")

                    sleep(1)

                    print("\nThe dealer will draw again!")

                    sleep(1)


        print("The dealer will stand.\n")

        print("Dealer's final hand:...\n")
        print(self.dealer)

        # If the dealer and the player have the same score
        if (self.dealer.score == self.player.score):

            print("\nGame is a tie!")
            # The game ends in a tie
            return "tie"

        # If the dealer's score is higher than the player's score
        elif (self.dealer.score > self.player.score):

            print("\nDealer wins!")
            # The dealer wins the game
            return "dealer win"

        # Player's score is greater than dealer's score
        else: 
            print("\nPlayer wins!")
            return "player win"



      

blackjackGame = Blackjack()
blackjackGame.play()
