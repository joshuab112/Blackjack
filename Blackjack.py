from time import sleep
from deck import Deck
from dealerHand import DealerHand
from playerHand import PlayerHand
from card import Card


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

        # Dealing out the initial cards to the dealer and player.
        # This variable determines the outcome of the initial card dealing.
        playerInitialDealingOutcome = self.initial_card_dealing()

        # If the player decides to split their hand (regardless of if they're two Aces)
        if (playerInitialDealingOutcome == "split no ace" or playerInitialDealingOutcome == "split ace"):

            # Create separate hand for left card
            leftPlayerHand = PlayerHand()

            print("Your left hand is a", end = " ")

            sleep(1)

            leftPlayerHand.hit(self.player.cards[0])

            sleep(1)

            # Create separate hand for right card
            rightPlayerHand = PlayerHand()

            print("Your right hand is a", end = " ")

            sleep(1)

            rightPlayerHand.hit(self.player.cards[1])

            sleep(1)

            # Players can only be dealt one card for each new hand if the identical hands contain Aces
            if (playerInitialDealingOutcome == "split ace"):

                print("Since you split Aces, you will only be dealt one card to each new hand...\n")

                sleep(1)

                print("New card for your left hand...", end = " ")

                sleep(1)

                # Hitting the player's left hand with a new card
                leftPlayerHand.hit(self.deck.deal_card())

                sleep(1)

                print("New left hand:\n")

                sleep(1)

                print(leftPlayerHand)

                sleep(1)

                # In the event a player gets another Ace and chooses to count it as 11
                if (leftPlayerHand.has_busted()):

                    self.outcome_of_player_turn("player bust", leftPlayerHand, "left")

                # If the player got a blackjack as a result of the newly dealt card
                elif (leftPlayerHand.score == 21):

                    self.outcome_of_player_turn("player blackjack", leftPlayerHand, "left")

                # The player is forced to stay since only one card can be dealt with split Aces
                else:
                    self.outcome_of_player_turn("stay", leftPlayerHand, "left")

                sleep(1)

                print("Let's deal a new card for your right hand...")

                sleep(1)

                print("\nNew card for your right hand...", end = " ")

                sleep(1)

                # Hitting the player's right hand with a new card
                rightPlayerHand.hit(self.deck.deal_card())

                sleep(1)

                print("New right hand:\n")

                sleep(1)

                # Showing the player their new right hand
                print(rightPlayerHand)

                sleep(1)

                # In the event a player gets another Ace and chooses to count it as 11
                if (rightPlayerHand.has_busted()):

                    self.outcome_of_player_turn("player bust", rightPlayerHand, "right")

                # If the player got a blackjack as a result of the newly dealt card
                elif (rightPlayerHand.score == 21):

                    self.outcome_of_player_turn("player blackjack", rightPlayerHand, "right")

                # The player is forced to stay since only one card can be dealt with split Aces
                else:
                    self.outcome_of_player_turn("stay", rightPlayerHand, "right")

            # Player's split cards are not Aces and thus their split hands can be played normally
            else:
                print("Let's play your left hand first...\n")

                sleep(1)

                print(leftPlayerHand)

                sleep(1)

                # Outcome of the player's left hand being played
                playerTurnOutcome_1 = self.player_turn(leftPlayerHand)

                # Respond accordingly to the result of the player's left hand being played
                self.outcome_of_player_turn(playerTurnOutcome_1, leftPlayerHand, "left")

                sleep(1)

                print("Now let's play your right hand...\n")

                sleep(1)

                print(rightPlayerHand)

                sleep(1)

                # Outcome of the player's right hand being played
                playerTurnOutcome_2 = self.player_turn(rightPlayerHand)

                # Respond accordingly to the result of the player's right hand being played
                self.outcome_of_player_turn(playerTurnOutcome_2, rightPlayerHand, "right")
            
            sleep(1)

            # It is time for the dealer to play since both of the player's split hands have played
            self.dealer_turn()

            sleep(1)

            # Evaluating the player's left hand against the dealer's hand
            self.game_result(leftPlayerHand, "left")

            sleep(1)
        
            # Evaluating the player's right hand against the dealer's hand
            self.game_result(rightPlayerHand, "right")

        # Player got a blackjack during their initial card dealing
        elif (playerInitialDealingOutcome == "player blackjack"):

            sleep(1)

            self.outcome_of_player_turn("player blackjack", self.player, "original")

            sleep(1)

            # It is time for the dealer to play
            self.dealer_turn()

            sleep(1)

            # Evaluate the player's blackjack against the dealer's hand
            self.game_result(self.player, "original")


        # In the event that a player gets two Aces and decides to count them both as 11
        elif (playerInitialDealingOutcome == "player bust"):

            sleep(1)

            self.outcome_of_player_turn("player bust", self.player, "original")

            # It is time for the dealer to play. Sole reason for dealer playing in the event of 
            # a player busting in the intial card dealing is so results are evaluated in the same function
            self.dealer_turn()

            sleep(1)

            # Even though player will inevitably lose, it's still important to keep result calculations in one function
            self.game_result(self.player, "original")

        # Player did not split and will play their original hand
        else:

            # Outcome of the player's original hand being played
            playerTurnOutcome = self.player_turn(self.player)

            sleep(1)

            # Respond accordingly to the result of the player's original hand being played
            self.outcome_of_player_turn(playerTurnOutcome, self.player, "original")

            sleep(1)

            # It is time for the dealer to play
            self.dealer_turn()

            sleep(1)

            # Evaluate the player's original hand against the dealer
            self.game_result(self.player, "original")


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

        # If the player has not busted and was dealt two cards with identical ranks
        if (self.player_can_split() and not self.player.has_busted()):

            # The player must decide whether or not to split their cards
            return self.player_split_decision()

        # In the event a player is given two Aces and chooses to count them both as 11
        elif (self.player.has_busted()):

            return "player bust"

        # If the player gets a natural 21 from their dealt cards
        elif (self.player.score == 21):

            return "player blackjack"

        # Player did not get a blackjack and is not able to split
        else:
            return "no split"


    # Function that activates the player's turn.
    # Returns "bust" if the player has busted or "stay" if
    # the player chose to stay.
    def player_turn(self, playerHand):

        while True:

            # Giving player the choice to hit or stay
            playerChoice = input("\nDo you wish to hit or stay (hit/stay)? ")

            # If the player chooses to hit
            if (playerChoice.lower() == "hit"):

                sleep(1)

                print("\nThe dealer will hit you with another card.")

                sleep(1)
                
                print ("\nYour new card...", end = " ")

                sleep(1)

                # Hitting the player with another card
                playerHand.hit(self.deck.deal_card())

                sleep(1)

                # Showing the player their new hand
                print("Here's your new hand:\n")

                sleep(1)

                print(f"{playerHand}")

                sleep(1)

                # If the player's new hand made them bust
                if (playerHand.has_busted()):

                    return "player bust"  
                
                # If player's new hand brings their score to 21
                elif (playerHand.score == 21):

                    return "player blackjack"

            # If the player chooses to stay
            elif (playerChoice.lower() == "stay"):

                return "stay"

            else:
                print("\nPlease select a valid choice")


    # Function that responds to the end of a player's turn according to 
    # the outcome of said player's turn (i.e., if they stayed, busted, or got a blackjack). 
    # The corresponding hand is passed in along with the hand's identification (i.e, left, right, or original)
    def outcome_of_player_turn(self, playerTurnResult, playerHand, playerHandID):

        # If the player's hand busted during their turn
        if (playerTurnResult == "player bust"):
            
            print("\nOh no! You've busted!\n")

        # If the player did not bust and chose to stay
        elif (playerTurnResult == "stay"):

            print(f"\nYour {playerHandID} hand has a final score of {playerHand.score}\n")

            sleep(1)

            # If the player is on their last hand then the dealer will play
            if (playerHandID == "original" or playerHandID == "right"):

                print("You will now stay.")

        # Player got a blackjack
        else:
            print("\nYou got a blackjack!")



    # Function that activates the dealer's turn.
    def dealer_turn(self):

        print("\nLet's see the dealer's hand...\n")

        sleep(2)

        print(self.dealer)

        sleep(2)

        # Dealer can only stand if their score is higher than 17 but less than 21
        if (self.dealer.score < 17):

            print("\nDealer's score is less than 17 so they must hit!\n")

            # Dealer must draw until their score is 17 or above
            while (self.dealer.score < 17):

                sleep(2)

                print("Dealer's new card...", end = " ")

                # Giving the dealer a new card
                self.dealer.hit(self.deck.deal_card())

                # Showing the dealer's new card
                print(f"{self.dealer.cards[-1]}\n")

                sleep(2)

                # If dealer's score is less than 17 after being given new card
                if (self.dealer.score < 17):

                    print(f"Dealer's score of {self.dealer.score} is still less than 17.")

                    sleep(2)

                    print("\nThe dealer will draw again!\n")

        print("The dealer will stay.\n")

        sleep(2)

        print("Dealer's final hand...\n")

        sleep(2)

        print(self.dealer)

        sleep(2)

        print(f"\n|Dealer's final score: {self.dealer.score}|\n")

    
    # Function that checks whether a player is eligible for a split
    def player_can_split(self):

        # If the player's two cards have the same rank
        if (self.player.cards[0]._rank == self.player.cards[1]._rank):
            return True

        # Player cannot split because their card ranks are not identical
        return False


    # Function that asks the player whether or not they would like to split their hand
    # and returns the choice the player makes
    def player_split_decision(self):

        sleep(1)
        
        print("\nLooks like you have identical ranks!")

        sleep(1)

        while(True):

            playerChoice = input("\nWould you like to split your hand (yes/no)? ")

            # Player chooses to split their hand
            if (playerChoice.lower().strip() == "yes"):

                sleep(1)

                print("\nYour current hand will be split!\n")

                sleep(1)

                # If the two cards being split are Aces and the player hasn't busted
                if (self.player.cards[0]._rank == "Ace" and self.player.cards[1]._rank == "Ace"):

                    # Player decides to split two Aces and will only be hit with one card for each split hand
                    return "split ace"

                else:
                    # Player decides to not split the Aces
                    return "split no ace"

            # Player chooses to not split and keeps their original hand
            elif (playerChoice.lower().strip() == "no"):

                sleep(1)

                print("\nYou have decided to play your original hand.")

                sleep(1)

                return "no split"

            else:
                print("\nPlease select a valid choice")


    # Function that calculates and returns the result of the game.
    # The hand being evaluated against the dealer's hand is passed in along with the ID of said hand. 
    def game_result(self, playerHand, playerHandID):

        print(f"\nPlayer's {playerHandID} hand has a final score of {playerHand.score}.\n")

        sleep(1)

        # If dealer's hand has busted and player's hand has not then that had beats the dealer
        if (self.dealer.has_busted() and not(playerHand.has_busted())):

            print(f"Dealer's hand has busted so player's {playerHandID} hand wins!\n")

        # If dealer's hand has not busted but the player's hand has busted
        elif (not(self.dealer.has_busted()) and playerHand.has_busted()):

            print(f"Player's {playerHandID} hand has busted therefore the dealer's hand wins.\n")

        elif (self.dealer.has_busted() and playerHand.has_busted()):

            print(f"Even though the dealer's hand busted, the player's {playerHandID} still loses against the dealer's hand")

        # Neither the dealer nor the player's hand busted
        else:

            # If the player got a 21 but the dealer did not
            if (playerHand.score == 21 and not(self.dealer.score == 21)):

                print(f"Since Player's {playerHandID} hand has a blackjack...player's {playerHandID} hand wins against the dealer's hand!\n")

                # The player wins the game
                return "player win"

            # If the dealer got a 21 but the player did not
            elif (not(playerHand.score == 21) and self.dealer.score == 21):

                print(f"Since dealer has a blackjack...Dealer wins against player's {playerHandID} hand!\n")

                # The dealer wins the game
                return "dealer win"

            # If the dealer and the player have the same score
            elif (self.dealer.score == playerHand.score):

                print(f"Player's {playerHandID} hand ties with dealer!\n")

                # The game ends in a tie
                return "tie"

            # If the dealer's score is higher than the player's score
            elif (self.dealer.score > playerHand.score):

                print(f"Dealer wins against player's {playerHandID} hand!\n")

                # The dealer wins the game
                return "dealer win"

            # Player's score is greater than dealer's score
            else: 
                print(f"Player's {playerHandID} hand wins!\n")

                # The player wins the game
                return "player win"


blackjackGame = Blackjack()
blackjackGame.play()
