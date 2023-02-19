from enum import Enum
from spritesheet import SpriteSheet

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

class Card:
    def __init__(self, card_game):
        # Card attributes
        self.image = None
        self.value = ''
        self.suit = ''

        self.screen = card_game.screen

        # Start each card in the top left corner
        self.x, self.y = 0.0, 0.0

    def blitme(self):
        # Draw the card at its current location
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y
        self.screen.blit(self.image, self.rect)

class Deck:
    # Set of Cards that are object of the Card class
    def __init__(self, card_game):
        # Initialize card attributes for all cards in the deck
        self.card_game = card_game
        self.cards = []
        self._load_cards()

    def _load_cards(self):
        # Builds the overall Deck
        # Loads images from sprite sheet
        # Create a card and assigns its attributes
        # Adds card to the deck

        filename = 'playing_cards.bmp'
        card_ss = SpriteSheet(filename)

        # Loads all card images
        card_images = card_ss.load_grid_images(5, 13, x_margin=0, x_padding=0, y_margin=0, y_padding=0)

        # # Create an Ace of Clubs
        # ace_clubs_rect = (0, 0, 147, 229)
        # ace_clubs_image = card_ss.image_at(ace_clubs_rect)

        # ace_clubs = Card(self.card_game)
        # ace_clubs.image = ace_clubs_image
        # ace_clubs.value = 'Ace'
        # ace_clubs.suit = 'Clubs'
        # self.cards.append(ace_clubs)

        # #Create a new Card object for every image
        # for image in card_images:
        #     card = Card(self.card_game)
        #     card.image = image
        #     self.cards.append(card)

        # Create a card for each image
        card_num = 0
        for suit in Suit:
            for value in Value:
                card = Card(self.card_game)
                card.value = value
                card.suit = suit
                card.image = card_images[card_num]
                self.cards.append(card)


                card_num += 1





