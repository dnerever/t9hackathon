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

class Card():
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

deck = []
deckOfCards = []
for i in range(4):      #need make this dynamic to allow multiple decks to be used
    for j in range(13):
        deck.append((Value(j+1).name, Suit(i).name))
        tempCard = Card(Value(j+1).name, Suit(i).name)
        deckOfCards.append(tempCard)

def shuffle():
    random.shuffle(deck)

def deal():
    return deck.pop(0)

def dealRound(numOfHands):
    hands = [[] for i in range(numOfHands)]
    for i in range(numOfHands):
        hands[i].append(deal())
    for i2 in range(numOfHands):
        hands[i2].append(deal())
    return hands

print("--------------------")
print("Dealt card: ", deal())
print("--------------------")
round1 = dealRound(5)
print("Round dealt", round1)



# card1 = Card(Value(j+1).name, Suit(i).name)
print("--------------------Here")
# print(card1.suit, " OF ", card1.value)
print("--------------------")

for i in range(52):
    print(deckOfCards[i].value, " OF ", deckOfCards[i].suit)


# Card()