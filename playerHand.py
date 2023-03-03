from hand import Hand
from card import Card

'''
Class that represents a player's hand of cards.
Unlike the dealer, when a player is dealt an Ace,
they can choose the value of said Ace. 
'''
class PlayerHand(Hand):
    
    def __init__(self):
        Hand.__init__(self)


    # Function that "hits", or adds a card to, a player's hand.
    # The value of the hand is updated accordingly.
    def hit(self, card):

        # Put the card in the player's hand
        self.cards.append(card)

        # Showing the player their card
        print(f"{card}\n")

        # If the card dealt is an Ace
        if (card._rank == "Ace"):


            while (True):

                # The player must choose whether to count the Ace as a 1 or 11
                optionalScore = input("Do you want to count the Ace as 1 or 11? ")

                # If the player enters any number besides 1 or 11
                if (optionalScore != "1" and optionalScore != "11"):

                    # Prompt the player for valid input
                    print("\nAce can only count as 1 or 11!\n")

                else:

                    # Player has chosen a valid score value
                    print("\n" + optionalScore + " it is!\n")

                    # Add the chosen score to the hand's score value
                    self.score += int(optionalScore)

                    break
                
        else: 
            self.score += Card.values[card._rank]




