import random
from enum import Enum
from spritesheet import SpriteSheet

class Suit(Enum):
    SPADES = 0
    HEARTS = 1
    CLUBS = 2
    DIAMONDS = 3

class Type(Enum):
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
    def __init__(self, type, suit, card_game):
        self.type = type
        self.suit = suit
        self.image = None
        self.screen = card_game.screen

        # Start each card in the top left corner
        self.x, self.y = 0.0, 0.0

    def blitme(self):
        # Draw the card at its current location
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y
        self.screen.blit(self.image, self.rect)
        
    def getType(self):
        return self.type.value
    
    def getSuit(self):
        return self.suit.value

    def compare(self, otherCard):
        return ((self.getType() == otherCard.getType()))

    def printCard(self):                        #error also prints "None" following expected output
        print("[", self.type.name, " OF ", self.suit.name, end="], ")

class Deck():
    def __init__(self, numOfDecks, card_game):
        self.card_game = card_game
        
        self.deck = []  # equivalent self.cards = []
        filename = 'images/playing_cards.bmp'
        self.card_ss = SpriteSheet(filename)
        # Loads all card images
        self.card_images = self.card_ss.load_grid_images(5, 13, x_margin=0, x_padding=0, y_margin=0, y_padding=0)
        self.card_back = self.card_images[54]
        for i in range(numOfDecks):
            card_num = 0
            for j  in range(len(Suit)):
                for k in range(len(Type)):
                    card = Card(Type(k+1), Suit(j), self.card_game)
                    # card.value = value
                    # card.suit = suit
                    card.image = self.card_images[card_num]
                    self.deck.append(card)
                    card_num += 1

    def deal(self):
        return self.deck.pop(0)

    def shuffle(self):
        random.shuffle(self.deck)

class Game():
    def __init__(self, numOfDecks, card_game):
        self.deck = Deck(numOfDecks, card_game)
        self.hands = [[]]

    def dealRound(self, numOfHands):
        self.clearHands()
        self.hands = [[] for i in range(numOfHands)]
        self.dealerHand = len(self.hands) - 1
        for i in range(numOfHands):
            self.hands[i].append(self.deck.deal())
        for i2 in range(numOfHands):
            self.hands[i2].append(self.deck.deal())

        self.reveal = False
        return self.hands

    def printHands(self):
        for i in range(len(self.hands)):
            for j in range(len(self.hands[i])):  #len(self.hands[i])     not working for case of having a single card
                self.hands[i][j].printCard()

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
                return upperVal
        else:
            if(upperVal > 21):
                return lowerVal
            else:
                return upperVal

    def bustOrBJ(self, handIndex):      # 1 = BJ, 0 = neither, -1 = bust/loss
        if((len(self.hands[handIndex]) == 2) and (self.handValue(handIndex) == 21)):
            print("**********Blackjack**********")
            return 1
        elif((self.handValue(handIndex)) > 21):
            print("**********Bust**********")
            return -1
        else:
            print("**********NO Blackjack or Bust**********")
            return 0

    def checkWin(self, handIndex):       # 1 = win, 0 = push/tie, -1 = loss
        dealerValue = self.handValue(self.dealerHand)
        playerValue = self.handValue(handIndex)
        if(self.bustOrBJ(handIndex)):
            return -1
        elif((dealerValue > 21 and (playerValue <= 21))):
            return 1
        
        if(playerValue > dealerValue):
            print("WIN")
            return 1
        elif((playerValue == dealerValue)):
            print("PUSH")
            return 0
        else:
            print("LOSS")
            return -1

    def hit(self, handIndex):
        self.hands[handIndex].append(self.deck.deal())

    def stand(self):
        return  # do nothing

    def split(self, hand):  #need to add case to check split possibility
        if(self.hands[hand][0].compare(self.hands[hand][1])):   #checks that the two cards are the same type
            newHandIndex = len(self.hands) #index of the new 2nd hand
            tempCard = [self.hands[hand].pop(0)]
            self.hands.append(tempCard)
            self.hit(hand)
            self.hit(newHandIndex)
            # print(self.printHands())
            return newHandIndex
        else:
            print("---This hand cannot be split---")
            return hand

    # def double():

    # def surrender():

    def dealerPlay(self):
        dealerValue = self.handValue(self.dealerHand)
        while(dealerValue < 17):
            self.hit(self.dealerHand)
            dealerValue = self.handValue(self.dealerHand)
        self.reveal = True

    def clearHands(self):
        for i in range(len(self.hands) - 1):
            self.hands[i].pop(0)