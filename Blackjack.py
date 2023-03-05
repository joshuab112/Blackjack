import math
from time import sleep
from Deck import Deck
from DealerHand import DealerHand
from PlayerHand import PlayerHand

'''
Class that will act as the main hub for the blackjack game.
Each game is initialized with a dealer, a player, 100 tokens for the player,
and a shuffled deck of cards.It should be noted that the dealer and 
and player are represented by their respective hand of cards. 
'''
class Blackjack(object):

    def __init__(self):
        self.deck = Deck()
        self.dealer = DealerHand()
        self.player = PlayerHand()
        self.tokens = 100


    # Function that sets up the game. Set up consists of checking whether the player has 
    # enough tokens to play the game, and if so, how many tokens they would like to bet.
    # Dealer and player scores and cards are reinitialized incase they have values from a previous game
    def setup(self):

        self.player = PlayerHand()
        self.dealer = DealerHand()

        print("--------------------------------------------------------------------")

        print("Welcome to Blackjack!\n")
        sleep(1.5)
        sleep(1.5)

        # If player is eligible to play the game
        if (self.player_can_play()):

            # Get the players bet and subtract it from their current amount of tokens
            self.get_player_bet()

            # Game can now be started
            self.play()
            
        # Player does not have enough tokens to play the game
        else:

            print("You don't have enough tokens to play. Apologies. Have a good day!\n")


    # Function that plays the main game once a player has placed their bet (if eligible to do so)
    def play(self):

        print("--------------------------------------------------------------------")
        print("Let the game begin!\n")

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

            print("Your original bet will now apply to both hands.\n")
            sleep(1)

            # Set bet value for left hand
            leftPlayerHand.bet = self.player.bet

            print(f"The bet for the left hand: {leftPlayerHand.bet} tokens.\n")
            sleep(1)

            # Set bet value for right hand
            rightPlayerHand.bet = self.player.bet

            print(f"The bet for the right hand: {rightPlayerHand.bet} tokens.\n")
            sleep(1)

            # Subtract additional bet from the total tokens since the player has split their hand
            self.tokens -= self.player.bet

            print(f"You now have {self.tokens} tokens.\n")
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
            sleep(1)

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

        # Giving player the choice to restart or end the game
        self.end_or_restart_game()


    # Function that checks whether or not the player has 2 or more tokens.
    # Player needs at least 2 tokens in order to play the game.
    def player_can_play(self):

        # If player has 2 or more tokens
        if (self.tokens > 1):

            # Player is able to play the game
            return True

        # Player has less than two tokens
        return False


    # Function that prompts the player for a bet amount and subtracts the amount of money
    # bet from their current amount of money
    def get_player_bet(self):

        while True:

            playerBet = input("How many tokens would you like to bet (minimum of 2 tokens)? ")

            # Checking to see if the input is a number that is 2 or more and is less than or equal to current token amount
            if (playerBet.isnumeric() and int(playerBet) >= 2 and int(playerBet) <= self.tokens):

                print(f"\nYou have chosen to bet {playerBet} tokens.\n")
                sleep(1)

                # Subtracting the player's bet from their current token amount
                self.tokens -= int(playerBet)

                # Setting the player's bet to the value that they chose to bet
                self.player.bet = int(playerBet)

                print(f"You now have {self.tokens} tokens left.\n")
                sleep(1)

                return

            # Player has placed a bet that is less than 2 tokens
            elif (playerBet.isnumeric() and int(playerBet) < 2):

                sleep(1)
                print("\nBet must be at least 2 tokens!\n")
                sleep(1)

            # Player has bet more tokens than they currently have
            elif (playerBet.isnumeric() and int(playerBet) > self.tokens):

                sleep(1)
                print("\nYou don't have enough tokens to place that bet!\n")
                sleep(1)

            else:
                sleep(1)
                print("\nPlease provide a valid number\n")
                sleep(1)


    # Function that deals out 2 cards to the player and the dealer.
    # The result of the player's given hand is returned.
    # These results include player deciding whether or not to split, or the player's hand busting or being a blackjack
    def initial_card_dealing(self):

        # Giving the player their first card
        print("Your first card...", end = " ")
        sleep(1)
        self.player.hit(self.deck.deal_card())
        sleep(1)

        # Giving the dealer their first card
        print("Dealer's first card...", end = " ")
        sleep(1)
        self.dealer.hit(self.deck.deal_card())

        # Showing the dealer's first card
        print(f"{self.dealer.cards[0]}\n")
        sleep(1)

        # Giving the player their second card
        print("Your second card...", end = " ")
        sleep(1)
        self.player.hit(self.deck.deal_card())
        sleep(1)

        # Giving the dealer their second card
        print("Dealer's second card...", end = " ")
        self.dealer.hit(self.deck.deal_card())
        sleep(1)

        # Player is not able to see what the dealer's second card is
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

                # Giving the dealer a new card
                print("Dealer's new card...", end = " ")
                self.dealer.hit(self.deck.deal_card())

                # Showing the dealer's new card
                print(f"{self.dealer.cards[-1]}\n")
                sleep(2)

                # If dealer's score is less than 17 after being given new card
                if (self.dealer.score < 17):

                    print(f"Dealer's score of {self.dealer.score} is still less than 17.")
                    sleep(2)
                    print("\nThe dealer will draw again!\n")

        # If the dealer has busted during their turn
        if (self.dealer.has_busted()):

            print ("Dealer has busted!\n")


         # Dealer did not bust during their turn
        else:
            print("The dealer will stay.\n")

        # Displaying the dealer's final hand
        sleep(2)
        print("Dealer's final hand...\n")
        sleep(2)
        print(self.dealer)

        # Displaying the dealer's final score
        sleep(2)
        print(f"\n|Dealer's final score: {self.dealer.score}|\n")

    
    # Function that checks whether a player is eligible for a split
    def player_can_split(self):

        # If the player's two cards have the same rank
        if (self.player.cards[0]._rank == self.player.cards[1]._rank):

            # Player must also have the right amount of tokens (2x the bet they placed)
            if ((self.player.bet * 2) <= self.tokens):

                return True

            # Players cards match but they have insufficient tokens to bet for split
            else:

                sleep(1)
                print ("\nUnfortunately, you do not have enough tokens to split these cards.\n")
                sleep(1)

                return False

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
    # Tokens are awarded if player's hand wins.
    def game_result(self, playerHand, playerHandID):

        print(f"\nPlayer's {playerHandID} hand has a final score of {playerHand.score}.\n")

        sleep(1)

        # If dealer's hand has busted and player's hand has not then that had beats the dealer
        if (self.dealer.has_busted() and not(playerHand.has_busted())):

            print(f"Dealer's hand has busted so player's {playerHandID} hand wins!\n")
            sleep(1)
            print(f"You have won {2 * playerHand.bet} tokens!\n")

            # Adding the awarded tokens to the player's total amount of tokens
            self.tokens += (2 * playerHand.bet)

        # If dealer's hand has not busted but the player's hand has busted
        elif (not(self.dealer.has_busted()) and playerHand.has_busted()):

            print(f"Player's {playerHandID} hand has busted therefore the dealer's hand wins.\n")
            sleep(1)
            print(f"The dealer will keep your bet of {playerHand.bet} tokens.\n")
        
        # If both the dealer's hand and the player's hand busted then the dealer still wins
        elif (self.dealer.has_busted() and playerHand.has_busted()):

            print(f"Even though the dealer's hand busted, the player's {playerHandID} hand still loses against the dealer's hand.\n")
            sleep(1)
            print(f"The dealer will keep your token bet of {playerHand.bet} tokens.\n")

        # Neither the dealer nor the player's hand busted
        else:

            # If the player got a 21 but the dealer did not then the player wins
            if (playerHand.score == 21 and not(self.dealer.score == 21)):

                print(f"Player's {playerHandID} hand has a blackjack...player's {playerHandID} hand wins against the dealer's hand!\n")

                sleep(1)

                # Blackjacks on split hands have a payout equivalent to that of a normal win on an unsplit hand
                if (playerHandID == "left" or playerHandID == "right"):

                    # Adding the awarded tokens to the player's total amount of tokens
                    self.tokens += (playerHand.bet)

                    print("Since blackjack was won on split hand, the payout is only 1:1.\n")
                    print(f"You still win {playerHand.bet} tokens!")

                else:
                    print(f"You have won {math.floor(playerHand.bet + (playerHand.bet * 1.5))} tokens!\n")

                    # Adding the awarded tokens to the player's total amount of tokens
                    self.tokens += math.floor((playerHand.bet + (playerHand.bet * 1.5)))

            # If the dealer got a 21 but the player did not then the dealer wins
            elif (not(playerHand.score == 21) and self.dealer.score == 21):

                print(f"Since dealer has a blackjack...Dealer wins against player's {playerHandID} hand!\n")
                sleep(1)
                print(f"The dealer will keep your bet of {playerHand.bet} tokens.\n")

            # If the dealer and the player have the same score then game ends in a tie
            elif (self.dealer.score == playerHand.score):

                print(f"Player's {playerHandID} hand ties with dealer!\n")
                sleep(1)
                print(f"Your bet of {playerHand.bet} tokens will be refunded.\n")

                self.tokens += playerHand.bet

            # If the dealer's score is higher than the player's score then the dealer wins
            elif (self.dealer.score > playerHand.score):

                print(f"Dealer wins against player's {playerHandID} hand!\n")
                sleep(1)
                print(f"The dealer will keep your bet of {playerHand.bet} tokens.\n")

            # Player's score is greater than dealer's score so the player wins
            else: 
                print(f"You have won {2 * playerHand.bet} tokens!\n")

                # Adding the awarded tokens to the player's total amount of tokens
                self.tokens += (2 * playerHand.bet)


        # Notifying the player how many tokens they have after the end of the game
        print(f"Now you have {self.tokens} tokens.\n")

     
    # Function that asks the player if they would like to end or restart the game.
    # If the player chooses to play again then the game will be setup.
    def end_or_restart_game(self):
        
        while True:

            # Asking the user if they would like to restart or end the game
            playerChoice = input("Would you like to play again (yes/no)? ")

            # Player chooses to restart the game
            if (playerChoice == "yes"):

                sleep(1)
                print("\nLet's go!\n")
                sleep(1)

                # Setting up for another game
                self.setup()
                sleep(1)

                break
            
            # Player chooses to end the game
            elif (playerChoice == "no"):

                print("\nHave a good day!\n")

                break

            else:
                sleep(1)
                print("Please provide a valid answer.")
                sleep(1)



# Creating a Blackjack object
blackjackGame = Blackjack()

# Setup the first blackjack game
blackjackGame.setup()
