from hand import Hand
from card import Card

'''
Class that represents a dealer's hand of cards.
What makes a dealer's hand unique is how the value 
of an Ace is calculated. Whereas a player gets
to choose the value of an Ace, an Ace's value
for the dealer is automatically chosen to produce the 
best outcome for the dealer.
'''
class DealerHand(Hand):

    def __init__(self):
        Hand.__init__(self)


    # Function that "hits", or gives a card to, the dealer.
     # The value of the hand is updated accordingly.
    def hit(self, card):

        # Put the card in the dealer's hand
        self.cards.append(card)

        # If the card dealt is an Ace
        if (card._rank == "Ace"):

            # If the Ace is the first card the dealer is hit with
            if (len(self.cards) == 1):

                # Count the Ace as 11
                self.score += 11

            # If the Ace is the second card the dealer is hit with
            elif (len(self.cards) == 2):

                # If the previous card is not an Ace
                if (self.cards[0]._rank == "Ace"):

                    # Count the Ace as 11
                    self.score += 11

                # If the previous card is an Ace
                else:

                    # Count the Ace as 1 to ensure the dealer does not bust
                    self.score += 1
            
            # If the Ace is given to the dealer because his score is 
            # 16 or less (i.e., he's being given more than two cards)
            else:
                
                # If the dealer's current score is less than 6
                if (self.score < 6):

                    # Count the Ace as an 11 
                    self.score += 11

                # If the dealer's score is greater than or equal to 6
                else:

                    # If counting the Ace as an 11 makes the dealer's score 
                    # fall between 17 and 21
                    if ( 17 <= (self.score + 11) <= 21):

                        # Count the Ace as 11
                        self.score += 11

                    # Counting the Ace as an 11 will make the dealer bust
                    else:

                        # The Ace will be counted as 1
                        self.score += 1
        
        # The card given is not an Ace
        else:

            # Add its face value to the dealer's score
            self.score += Card.values[card._rank]


    # Function that only shows one of the dealer's cards and its corresponding score.
    # Used at the beginning of the game to hide dealer's second card from player.
    def obscured_hand(self):

        # Making the hand more presentable
        currentHand = "--------------------\n"
        
        currentHand += self.cards[0].__str__() + "\n{Hidden Card}"

        currentHandAndScore = currentHand + "\n\nScore of: ?"

        # Making the hand and score more presentable
        currentHandAndScore += "\n--------------------"

        return currentHandAndScore





            


    




