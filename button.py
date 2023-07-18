import pygame.font


class Button:

    def __init__(self, ai_game, msg):
        self.game_screen = ai_game.screen
        self.screen_rect = self.game_screen.get_rect()

        self.width = 300
        self.height = 80

        self.button_color = (0 ,255, 0)
        self.txt_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 50)

        self.rect = pygame.Rect(0, 0, self.width, self.height)

        self.rect.center = self.screen_rect.center

        self._set_msg(msg)

    def _set_msg(self, msg):
        self.img_msg = self.font.render(msg, True, self.txt_color, self.button_color)
        self.img_msg_rect = self.img_msg.get_rect()
        self.img_msg_rect.center = self.screen_rect.center

    def draw_button(self):
        self.game_screen.fill(self.button_color, self.rect)
        self.game_screen.blit(self.img_msg, self.img_msg_rect)