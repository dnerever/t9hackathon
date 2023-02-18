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

    def getValue(self):
        return self.value.value
    
    def getSuit(self):
        return self.suit.value

    def printCard(self):                        #error also prints "None" following expected output
        print(self.value.name, " OF ", self.suit.name)
        print("--------------------")

class Deck():
    def __init__(self, numOfDecks):
        self.deck = []
        for i  in range(4):
            for j in range(13):
                self.deck.append(Card(Value(j+1), Suit(i)))

    def deal(self):
        return self.deck.pop(0)

    def shuffle(self):
        random.shuffle(self.deck)

    def dealRound(self, numOfHands):
        self.hands = [[] for i in range(numOfHands)]
        for i in range(numOfHands):
            self.hands[i].append(self.deal())
        for i2 in range(numOfHands):
            self.hands[i2].append(self.deal())
        return self.hands

    def printHands(self):
        for i in range(len(self.hands)):
            print("Hand #", i, ": ")
            for j in range(len(self.hands[i])):
                self.hands[i][j].printCard()

# class Game():
#     def __init__(self, numOfDecks):


d1 = Deck(1)

d1.shuffle()
d1.dealRound(2)
print(d1.printHands())


# for i in range(52):
#     print(d1.deal().printCard())


