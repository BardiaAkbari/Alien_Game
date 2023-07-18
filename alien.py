import pygame
from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.alien_image = pygame.image.load(self.settings.alien_image)
        self.alien_image_rect = self.alien_image.get_rect()

        self.alien_image_rect.x = self.alien_image_rect.width
        self.alien_image_rect.y = self.alien_image_rect.height

        self.alien_x_position = float(self.alien_image_rect.x)

    def blit_alien(self):
        self.screen.blit(self.alien_image, self.alien_image_rect)
