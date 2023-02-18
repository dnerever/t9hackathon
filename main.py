import random
import array
from enum import Enum

class Suit(Enum):
    SPADES = 0
    HEARTS = 1
    CLUBS = 2
    DIAMONDS = 3

class Value(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13

deck = []

for i in range(4):
    for j in range(13):
        deck.append((Suit(i).name,Value(j+1).name))

print(deck)

def shuffle(deck):
    random.shuffle(deck)

def deal(deck):
    return deck.pop()

# shuffle(deck)
# print(deck)
print("Dealt card: ", deal(deck))
