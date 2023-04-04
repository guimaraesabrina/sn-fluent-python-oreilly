"""
A method with two underscores at the beginning and end of its name is called a "magic method" or "special method".

These methods are used to define special behavior of objects in specific situations.

These methods are called automatically by the Python interpreter in specific situations and can be very useful for customizing the behavior of objects in your application.

For example, the '__getitem__' method is used to define the behavior of an object when an element is accessed through the indexing operator []

__len__
__str__
__init__
__eq__
__lt__, __gt__, __le__, __ge__

Possible names:
under-under-method
magic-method
double-underscore-method
"""

import collections

card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in list(range(2, 11)) + list('JQKA')]

    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
    
    def __len__(self):
        return len(self._cards)
    
    def __getittem__(self, position):
        return self._cards[position]

"""
1. 'import collections' = Imports the collections module, which contains several useful data structures.

2. 'card = collections.namedtuple('Card', ['rank', 'suit'])' = Creates a namedtuple called Card with two fields: 'rank' and 'suit'. namedtuple is a tuple subclass that allows you to access its elements by name.

In this case, we are creating something like: Card(rank=None, suit=None)

3. 'class FrenchDeck:' = Defines a new class called FrenchDeck.

4. 'ranks = ranks = [str(n) for n in list(range(2, 11)) + list('JQKA')]' Creates a list called ranks, which contains the ranks of the cards in ascending order, from 2 to 10, followed by the letters ' J', 'Q', 'K' and 'A' (Jack, Queen, King and Ace). (using list-comprehension)

"""