from enum import StrEnum
from random import shuffle

class Suit(StrEnum):
    SPADES = "S"
    HEARTS = "H"
    CLUBS = "C"
    DIAMONDS = "D"

class Rank(StrEnum):
    ACE = "A"
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    TEN = "10"
    JACK = "J"
    QUEEN = "Q"
    KING = "K"

class Card(object):
    def __init__(self, card_string):
        for r in Rank:
            if r in card_string:
                self.rank = r
        for s in Suit:
            if s in card_string:
                self.suit = s
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def __repr__(self):
        # return f"{self.rank}{self.suit}"
        return f"[{Rank(self.rank).name.title()} of {Suit(self.suit).name.title()}]"

class Deck(object):
    def __init__(self):
        self.cards = []
        self.dealt = []
        for r in Rank:
            for s in Suit:
                self.cards.append(Card(r, s))
        shuffle(self.cards)
    
    def deal(self, n=1):
        ret = []
        for _ in range(n):
            c = self.cards.pop()
            self.dealt.append(c)
            ret.append(c)
        return ret
    
    def reset(self):
        self.cards.extend(self.dealt)
        self.dealt = []
        shuffle(self.cards)
    
    def __repr__(self):
        return f"Deck of {len(self.cards)}"