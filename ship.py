import pygame
from pygame.sprite import Sprite


class Ship(Sprite):

    def __init__(self, ai_game):

        # Screen rectangle
        self.game_screen = ai_game.screen
        self.game_screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.ship_image = pygame.image.load(self.settings.ship_image)
        self.rect = self.ship_image.get_rect()
        # Ship set position
        self.rect.midbottom = self.game_screen_rect.midbottom
        # Moving Ship
        self.moving_right = False
        self.moving_left = False
        # Set settings
        self.settings = ai_game.settings
        # My ship position
        self.ship_x_position = float(self.rect.x)

    def update_moving(self):

        if self.moving_right and self.rect.right < self.game_screen_rect.right:
            self.ship_x_position += self.settings.ship_speed

        if self.moving_left and self.rect.left > self.game_screen_rect.left:
            self.ship_x_position -= self.settings.ship_speed

        self.rect.x = self.ship_x_position

    def blitme(self):

        self.game_screen.blit(self.ship_image, self.rect)

    def reset_ship(self):
        self.rect.midbottom = self.game_screen_rect.midbottom
        self.ship_x_position = float(self.rect.x)