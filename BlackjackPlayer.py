''' 
Class that represents any blackjack player.
That is, each player in blackjack will have a hand
of cards and a score associated with said hand. 
'''
class BlackjackPlayer(object):

    def __init__(self, hand):
        self._hand = hand

    # Function that checks whether a player's hand score is over 21
    def has_busted(self):
        if (self._hand._score > 21):
            return True

        return False







