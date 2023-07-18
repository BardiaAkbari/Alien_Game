import pygame
from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.alien_image = pygame.image.load(self.settings.alien_image)
        self.rect = self.alien_image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.alien_x_position = float(self.rect.x)

    def blit_alien(self):
        self.screen.blit(self.alien_image, self.rect)

    def update(self):
        global direction
        direction = 1

        if self.settings.fleet_direction == "Right":
            direction = 1
        else:
            direction = -1
        self.alien_x_position += self.settings.alien_speed * direction
        self.rect.x = self.alien_x_position
