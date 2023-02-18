import random
import array
from enum import Enum

class Suit(Enum):
    SPADES = 0
    HEARTS = 1
    CLUBS = 2
    DIAMONDS = 3

class Type(Enum):
    ACE = 1
    TWO = 2
    # THREE = 3
    # FOUR = 4
    # FIVE = 5
    # SIX = 6
    # SEVEN = 7
    # EIGHT = 8
    # NINE = 9
    # TEN = 10
    # JACK = 11
    # QUEEN = 12
    # KING = 13

class Card():
    def __init__(self, type, suit):
        self.type = type
        self.suit = suit
        # self.image

    def getType(self):
        return self.type.value
    
    def getSuit(self):
        return self.suit.value

    def compare(self, otherCard):
        return ((self.getType() == otherCard.getType()))

    def printCard(self):                        #error also prints "None" following expected output
        print("[", self.type.name, " OF ", self.suit.name, end="], ")
        # print("--------------------")

class Deck():
    def __init__(self, numOfDecks):
        self.deck = []
        for i in range(numOfDecks):
            for j  in range(len(Suit)):
                for k in range(len(Type)):
                    self.deck.append(Card(Type(k+1), Suit(j)))

    def deal(self):
        return self.deck.pop(0)

    def shuffle(self):
        random.shuffle(self.deck)

class Game():
    def __init__(self, numOfDecks):
        self.deck = Deck(numOfDecks)

    def dealRound(self, numOfHands):
        self.hands = [[] for i in range(numOfHands)]
        self.dealerHand = len(self.hands) - 1
        for i in range(numOfHands):
            self.hands[i].append(self.deck.deal())
        for i2 in range(numOfHands):
            self.hands[i2].append(self.deck.deal())
        return self.hands

    def printHands(self):
        for i in range(len(self.hands)):
            if(i == self.dealerHand):
                print("**Dealer Hand** ", end="")
            print("Hand #(", i, "): ", self.handValue(i))
            for j in range(len(self.hands[i])):  #len(self.hands[i])     not working for case of having a single card
                self.hands[i][j].printCard()
            print()

    def handValue(self, hand):
        upperVal = 0
        lowerVal = 0
        for i in range(len(self.hands[hand])):
            cardType = self.hands[hand][i].getType()
            if 2 < cardType and cardType <= 10:
                upperVal += cardType
                lowerVal += cardType
            elif cardType == 1:
                upperVal += 11
                lowerVal += 1
            else:
                upperVal += 10
                lowerVal += 10

        if(upperVal != lowerVal):
            if(upperVal > 21):
                return lowerVal
            else:
                return (upperVal, lowerVal)

        return upperVal

    def BustOrBJ(self, handIndex):
        if((len(self.hand[handIndex]) == 2) and (self.handValue(handIndex) == 21)):
            print("**********Blackjack**********")
            return True
        elif((self.handValue(handIndex)) > 21):
            print("**********Bust**********")
            return True
        else:
            print("**********NO Blackjack or Bust**********")
            return False

    # def check

    def hit(self, handIndex):
        self.hands[handIndex].append(self.deck.deal())

    def stand(self):
        return  # do nothing

    def split(self, hand):  #need to add case to check split possibility
        if(self.hands[hand][0].compare(self.hands[hand][1])):   #checks that the two cards are the same type
            newHandIndex = len(self.hands) #index of the new 2nd hand
            tempCard = [self.hands[hand].pop(0)]
            self.hands.append(tempCard)
            print("newHandIndex: ", newHandIndex)
            self.hit(hand)
            self.hit(newHandIndex)
            print(self.printHands())
            return newHandIndex
        else:
            print("---This hand cannot be split---")
            return hand

    # def double():
        

    # def surrender():


g1 = Game(2)

# print("comparison (false): ", g1.deck.deck[0].compare(g1.deck.deck[1]))
# print("comparison (true): ", g1.deck.deck[0].compare(g1.deck.deck[13]))

print(len(g1.deck.deck))

g1.deck.shuffle()
g1.dealRound(2)
print(g1.printHands())

g1.split(0)
g1.hit(0)

g1.printHands()
