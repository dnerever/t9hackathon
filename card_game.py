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

        #Improving readability
        self.screen_width = self.settings.screen_width
        self.screen_height = self.settings.screen_height
        self.buttonXPos = self.screen_width - 200
        self.button_width = 60
        self.button_color = (255,255,255)

        #[self.hit_hover, self.stand_hover, self.double_down_hover, self.split_hover, self.quit_hover]
        self.button_hover_list = [False, False, False, False, False]

        self.button_text_width = self.screen_width - 150


        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height)) 
        pygame.display.set_caption("Cards")

        # Button coloring
        text_color = (255, 255, 255)
        self.color_light = (170, 170, 170)
        self.color_dark = (100, 100, 100)
        smallfont = pygame.font.SysFont('Corbel', 35)
        self.hit_text = smallfont.render('Hit', True, text_color)
        self.quit_text = smallfont.render('Continue', True, text_color)
        self.stand_text = smallfont.render('Stand', True, text_color)
        self.split_text = smallfont.render('Split', True, text_color)
        self.double_down_text = smallfont.render('Double', True, text_color)
        self.button_text_list = [self.hit_text, self.stand_text, self.double_down_text, self.split_text, self.quit_text]
        self.button_y_shift = 100
        self.button_height = 40

        # self.g = Game(2, self)

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
                if event.key == pygame.K_s:
                    print("Standing")
                    self.g.stand()
                    self.g.dealerPlay()
            #If mouse is pressed
            self.mouse = pygame.mouse.get_pos()
            self.mouseX = self.mouse[0]
            self.mouseY = self.mouse[1]
            if event.type == pygame.MOUSEBUTTONDOWN:
                end_button_width = (self.screen_width - self.button_width)
                mouse_X_Over_buttonX = (self.buttonXPos <= self.mouseX <= end_button_width)     #checks if mouse is on x position of buttons
                
                if(mouse_X_Over_buttonX):
                    # On Hit
                    if(self.screen_height - self.button_y_shift*5 <= self.mouseY <= self.screen_height - (self.button_y_shift*5 - self.button_height)):
                        print("Hitting")
                        self.g.hit(0)
                    # On Stand
                    elif(self.screen_height - self.button_y_shift*4 <= self.mouseY <= self.screen_height - (self.button_y_shift*4 - self.button_height)):
                        print("Standing")
                        self.g.stand()
                        self.g.dealerPlay()
                        self.g.checkWin(0)       #add variable to check win
                    # On Double Down
                    elif(self.screen_height - self.button_y_shift*3 <= self.mouseY <= self.screen_height - (self.button_y_shift*3 - self.button_height)):
                        print("Doubling Down")
                    elif(self.screen_height - self.button_y_shift*2 <= self.mouseY <= self.screen_height - (self.button_y_shift*2 - self.button_height)):
                        print("Splitting")
                    # On Quit
                    elif(self.screen_height - self.button_y_shift <= self.mouseY <= self.screen_height - (self.button_y_shift - self.button_height)):
                        print("Quitting")
                        sys.exit()
        
        # Button interactions ------
        for i in range(len(self.button_hover_list)):
            self.button_hover_list[i] = False
            if (self.buttonXPos <= self.mouseX <= self.screen_width - self.button_width):
                if ((self.screen_height - self.button_y_shift * (5-i)) <= self.mouseY <= self.screen_height - (self.button_y_shift * (5-i) - self.button_height)):
                    self.button_hover_list[i] = True
            else:
                self.button_hover_list[i] = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)

        xShift = (self.screen_width - self.g.deck.card_ss.x_sprite_size)/2
        yShift = (self.screen_height - self.g.deck.card_ss.y_sprite_size)/2
        if self.g.reveal == False:
            self.g.hands[1][0].x = xShift
            self.g.hands[1][0].y = 70
            self.g.hands[1][0].blitme()
        else:
            for index, card in enumerate(self.g.hands[1]):
                card.x = xShift + index * 50
                card.y = 70
                card.blitme()
                # time.sleep(0.1)       //effects ALL visible actions

        for index, card in enumerate(self.g.hands[0]):
            card.x = xShift + index * 50
            card.y = 500
            card.blitme()

        # # Draw a row of clubs
        # for index, card in enumerate(self.deck_of_cards.cards[0:13]):
        #     card.x = index * 50
        #     card.blitme()

        #checks if mouse is over a button and changes color if true 
        for i in range(len(self.button_hover_list)):
            if self.button_hover_list[i] == True:
                pygame.draw.rect(self.screen,self.color_light,[self.buttonXPos, self.screen_height - (self.button_y_shift * (5-i)),140,40])
            else:
                pygame.draw.rect(self.screen,self.color_dark,[self.buttonXPos, self.screen_height - (self.button_y_shift * (5-i)),140,40])
            self.screen.blit(self.button_text_list[i], (self.button_text_width, self.screen_height - (self.button_y_shift * (5-i))))

        pygame.display.flip()
        pygame.display.update()

if __name__ == '__main__':
    card_game = CardGame()
    card_game.run_game()