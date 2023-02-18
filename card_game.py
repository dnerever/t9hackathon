import sys
import pygame
from main import *
from settings import Settings
import time
# from deck_of_cards import Deck
# from deck_of_cards import Card


class CardGame:
    # Overall class to manage game assets and behavior

    def __init__(self):
        # Initialize the game
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) 
        pygame.display.set_caption("Cards")

        # Button coloring
        text_color = (255, 255, 255)
        self.color_light = (170, 170, 170)
        self.color_dark = (100, 100, 100)
        smallfont = pygame.font.SysFont('Corbel', 35)
        self.hit_text = smallfont.render('Hit', True, text_color)
        self.quit_text = smallfont.render('Quit', True, text_color)
        self.stand_text = smallfont.render('Stand', True, text_color)
        self.split_text = smallfont.render('Split', True, text_color)
        self.double_down_text = smallfont.render('Double Down', True, text_color)
        self.button_y = 100
        self.button_height = 40

        self.g = Game(2, self)



    def run_game(self):
        # Start the game loop
        self.g = Game(2, self)
        self.g.deck.shuffle()
        self.g.dealRound(2)

        while True:
            self._check_events()
            self._update_screen()


    def _check_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    print("Quitting")
                    sys.exit()
            #If mouse is pressed
            self.mouse = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # On Quit button
                if (self.settings.screen_width - 200 <= self.mouse[0]
                <= self.settings.screen_width - 60):
                    if (self.settings.screen_height - self.button_y <= self.mouse[1]
                    <= self.settings.screen_height - (self.button_y - self.button_height)):
                        print("Quitting")
                        sys.exit()

                # On Hit button
                if (self.settings.screen_width - 200 <= self.mouse[0]
                <= self.settings.screen_width - 60):
                    if (self.settings.screen_height - self.button_y*5 <= self.mouse[1]
                    <= self.settings.screen_height - (self.button_y*5 - self.button_height)):
                        print("Hitting")
                        self.g.hit(0)


                # On Stand
                if (self.settings.screen_width - 200 <= self.mouse[0]
                <= self.settings.screen_width - 60):
                    if (self.settings.screen_height - self.button_y*4 <= self.mouse[1]
                    <= self.settings.screen_height - (self.button_y*4 - self.button_height)):
                        print("Standing")
                        self.g.stand()
                        self.g.dealerPlay()

                # On Double Down
                if (self.settings.screen_width - 200 <= self.mouse[0]
                <= self.settings.screen_width - 60):
                    if (self.settings.screen_height - self.button_y*3 <= self.mouse[1]
                    <= self.settings.screen_height - (self.button_y*3 - self.button_height)):
                        print("Doubling Down")


                # On Split
                if (self.settings.screen_width - 200 <= self.mouse[0]
                <= self.settings.screen_width - 60):
                    if (self.settings.screen_height - self.button_y*2 <= self.mouse[1]
                    <= self.settings.screen_height - (self.button_y*2 - self.button_height)):
                        print("Splitting")
        
        
        # Button interactions
        # Hovering on Quit button
        self.quit_hover = False
        if (self.settings.screen_width - 200 <= self.mouse[0]
        <= self.settings.screen_width - 60):
            if ((self.settings.screen_height - 100)
            <= self.mouse[1] <= self.settings.screen_height - 60):#(self.button_y - self.button_height)):
                self.quit_hover = True
        else:
            self.quit_hover = False

        # Hovering on Hit button
        self.hit_hover = False
        if (self.settings.screen_width - 200 <= self.mouse[0]
        <= self.settings.screen_width - 60):
            if ((self.settings.screen_height - self.button_y * 5)
            <= self.mouse[1] <= self.settings.screen_height - (self.button_y * 5 - self.button_height)):
                self.hit_hover = True
        else:
            self.hit_hover = False

        # Hovering on Stand button
        self.stand_hover = False
        if (self.settings.screen_width - 200 <= self.mouse[0]
        <= self.settings.screen_width - 60):
            if ((self.settings.screen_height - self.button_y * 4)
            <= self.mouse[1] <= self.settings.screen_height - (self.button_y * 4 - self.button_height)):
                self.stand_hover = True
        else:
            self.stand_hover = False

        # Hovering on Double Down button
        self.double_down_hover = False
        if (self.settings.screen_width - 200 <= self.mouse[0]
        <= self.settings.screen_width - 60):
            if ((self.settings.screen_height - self.button_y * 3)
            <= self.mouse[1] <= self.settings.screen_height - (self.button_y * 3 - self.button_height)):
                self.double_down_hover = True
        else:
            self.double_down_hover = False

        # Hovering on Split button
        self.split_hover = False
        if (self.settings.screen_width - 200 <= self.mouse[0]
        <= self.settings.screen_width - 60):
            if ((self.settings.screen_height - self.button_y * 2)
            <= self.mouse[1] <= self.settings.screen_height - (self.button_y * 2 - self.button_height)):
                self.split_hover = True
        else:
            self.split_hover = False
           

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)

        # # Draw the Ace of Clubs in its current position
        # self.deck_of_cards.cards[0].blitme()
        
        if self.g.reveal == False:
            self.g.hands[1][0].blitme()
        else:
            for index, card in enumerate(self.g.hands[1]):
                card.x = index * 50
                card.blitme()
                # time.sleep(0.5)

        for index, card in enumerate(self.g.hands[0]):
            card.x = index * 50
            card.y = 500
            card.blitme()

            
        # self.g.hands[0][0].blitme()
        
        # self.g.deck.deck[0].blitme()

        # # Draw a row of clubs
        # for index, card in enumerate(self.deck_of_cards.cards[0:13]):
        #     card.x = index * 50
        #     card.blitme()

        # # Draw a row of diamonds
        # for index, card in enumerate(self.deck_of_cards.cards[13:26]):
        #     card.x = index * 50
        #     card.y = 230
        #     card.blitme()

        # # Draw a row of hearts
        # for index, card in enumerate(self.deck_of_cards.cards[26:39]):
        #     card.x = index * 50
        #     card.y = 460
        #     card.blitme()

        # # Draw a row of spades
        # for index, card in enumerate(self.deck_of_cards.cards[39:52]):
        #     card.x = index * 50
        #     card.y = 690
        #     card.blitme()

        #Quit
        if self.quit_hover == True:
            pygame.draw.rect(self.screen,self.color_light,[self.settings.screen_width - 200,self.settings.screen_height - self.button_y,140,40])
        else:
             pygame.draw.rect(self.screen,self.color_dark,[self.settings.screen_width - 200,self.settings.screen_height - self.button_y,140,40])
        self.screen.blit(self.quit_text, (self.settings.screen_width - 160, self.settings.screen_height - self.button_y))

        # Hit
        if self.hit_hover == True:
            pygame.draw.rect(self.screen,self.color_light,[self.settings.screen_width - 200,self.settings.screen_height - (self.button_y * 5),140,40])
        else:
             pygame.draw.rect(self.screen,self.color_dark,[self.settings.screen_width - 200,self.settings.screen_height - (self.button_y * 5),140,40])
        self.screen.blit(self.hit_text, (self.settings.screen_width - 150, self.settings.screen_height - (self.button_y * 5)))

        # Stand
        if self.stand_hover == True:
            pygame.draw.rect(self.screen,self.color_light,[self.settings.screen_width - 200,self.settings.screen_height - (self.button_y * 4),140,40])
        else:
             pygame.draw.rect(self.screen,self.color_dark,[self.settings.screen_width - 200,self.settings.screen_height - (self.button_y * 4),140,40])
        self.screen.blit(self.stand_text, (self.settings.screen_width - 150, self.settings.screen_height - (self.button_y * 4)))

        # Double Down
        if self.double_down_hover == True:
            pygame.draw.rect(self.screen,self.color_light,[self.settings.screen_width - 200,self.settings.screen_height - (self.button_y * 3),140,40])
        else:
             pygame.draw.rect(self.screen,self.color_dark,[self.settings.screen_width - 200,self.settings.screen_height - (self.button_y * 3),140,40])
        self.screen.blit(self.double_down_text, (self.settings.screen_width - 150, self.settings.screen_height - (self.button_y * 3)))

        # Split
        if self.split_hover == True:
            pygame.draw.rect(self.screen,self.color_light,[self.settings.screen_width - 200,self.settings.screen_height - (self.button_y * 2),140,40])
        else:
             pygame.draw.rect(self.screen,self.color_dark,[self.settings.screen_width - 200,self.settings.screen_height - (self.button_y * 2),140,40])
        self.screen.blit(self.split_text, (self.settings.screen_width - 150, self.settings.screen_height - (self.button_y * 2)))


        pygame.display.flip()
        pygame.display.update()


if __name__ == '__main__':
    card_game = CardGame()
    card_game.run_game()