# French Deck.py

import collections
# Pick a random card
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    # Ranks is a list, [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'].
    # list('JQKA') seems to split string into list of separate letters. Yes.

    suits = 'spade diamond club heart'.split()
    # Default split string on space? Same as .split(' ')? Yes

    def __init__(self): 
        self._cards = [Card(rank, suit) for suit in self.suits 
                        for rank in self.ranks]

    def __len__(self): 
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


# Since python 2.6, "namedtuple" is commonly used to build simple 
# class objects without custom methods.                  ',

# Test Card object by initializing.
beer_card = Card('7', 'diamond')
print(beer_card)

my_card = Card('J', 'heart')
print(my_card)         # Card(rank='J', suit='heart')
print(my_card[0])      # J
print(my_card[1])      # heart

# Call class functions
deck = FrenchDeck()
len(deck)
print(deck[0:5])
print(deck[0:52:13])
print(deck[-1])

# Pick a random card
from random import choice
print(choice(deck))
print(choice(deck))
print(choice(deck))