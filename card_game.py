import sys
import pygame
from main import *
from settings import Settings
import time

# Overall class to manage game assets and behavior
class CardGame:
    def __init__(self):
        # Initialize the game
        pygame.init()
        self.settings = Settings()

        #Improving readability
        self.screen_width = self.settings.screen_width
        self.screen_height = self.settings.screen_height
        self.button_x_start = self.screen_width - 200
        self.button_width = 140
        self.button_x_end = self.button_x_start + self.button_width
        self.button_height = 40
        self.button_y_shift = 100
        self.mouse_x = -1
        self.mouse_y = -1
        self.button_color = (255,255,255)
        self.button_text_offset = 50
        self.button_x_text_pos = self.button_x_start + self.button_text_offset

        # set button's y start and ends
        self.button_y_start = []
        self.button_y_end = []
        for i in range(5):
            self.button_y_start.append(self.screen_height - self.button_y_shift*(5-i))
            self.button_y_end.append(self.button_y_start[i] + self.button_height)

        #[self.hit_hover, self.stand_hover, self.double_down_hover, self.split_hover, self.quit_hover]
        self.button_hover_list = [False, False, False, False, False]

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
            self._update_mouse_position()
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if(self._mouse_x_overlap(self.button_x_start, self.button_x_end)):
                    # On Hit
                    if(self._mouse_y_overlap(self.button_y_start[0], self.button_y_end[0])):
                        print("Hitting")
                        self.g.hit(0)
                    # On Stand
                    elif(self._mouse_y_overlap(self.button_y_start[1], self.button_y_end[1])):
                        print("Standing")
                        self.g.stand()
                        self.g.dealerPlay()
                        self.g.checkWin(0)       #add variable to check win
                    # On Double Down
                    elif(self._mouse_y_overlap(self.button_y_start[2], self.button_y_end[2])):
                        print("Doubling Down")
                    elif(self._mouse_y_overlap(self.button_y_start[3], self.button_y_end[3])):
                        print("Splitting")
                    # On Quit
                    elif(self._mouse_y_overlap(self.button_y_start[4], self.button_y_end[4])):
                        print("Quitting")
                        self.g.dealRound(2)
                        time.sleep(.01)
                        # sys.exit()
        
        # Button interactions ------
        for i in range(len(self.button_hover_list)):
            self.button_hover_list[i] = False
            if (self.button_x_start <= self.mouse_x <= self.button_x_end):
                if ((self.screen_height - self.button_y_shift * (5-i)) <= self.mouse_y <= self.screen_height - (self.button_y_shift * (5-i) - self.button_height)):
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
            # self.g.deck.card_back.blitme()
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
                pygame.draw.rect(self.screen,self.color_light,[self.button_x_start, self.button_y_start[i],self.button_width,self.button_height]) 
            else:
                pygame.draw.rect(self.screen,self.color_dark,[self.button_x_start, self.button_y_start[i],self.button_width,self.button_height])
            self.screen.blit(self.button_text_list[i], (self.button_x_text_pos, self.button_y_start[i]))

        pygame.display.flip()
        pygame.display.update()

    def _update_mouse_position(self):
        self.mouse_x = self.mouse[0]
        self.mouse_y = self.mouse[1]

    def _mouse_x_overlap(self, minPos, maxPos):
        return (minPos <= self.mouse_x <= maxPos)
    
    def _mouse_y_overlap(self, minPos, maxPos):
        return (minPos <= self.mouse_y <= maxPos)
        
if __name__ == '__main__':
    card_game = CardGame()
    card_game.run_game()