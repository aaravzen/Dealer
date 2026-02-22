from Gameplay.card import Card, Deck, Suit, Rank

class Table(object):
    def __init__(self):
        self.deck = Deck()
        self.players = []
        self.hands = []
        self.dealer = 0
    
    def add_player(self, player):
        self.players.append(player)
    
    def cleanup(self):
        self.hands = []
        self.dealer += 1

    def run_hand(self):
        for p in self.players:
            self.hands.append(self.deck.deal(2))
        
        # take blinds
        # pass priority
        # check end_conditions
        # assign pot

        self.cleanup()