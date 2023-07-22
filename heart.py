import pygame.image
from pygame.sprite import Sprite
from pygame.sprite import Group


class Heart(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.hearts = Group()
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.image = pygame.image.load(self.settings.heart_image)
        self.rect = self.image.get_rect()

    def render_heart(self, ai_game):
        self.hearts.empty()
        for heart_number in range(self.stats.ship_left):
            heart = Heart(ai_game)
            heart.rect.x = 10 + (heart_number * self.rect.width)
            heart.rect.y = 10
            self.hearts.add(heart)

    def draw(self):
        self.hearts.draw(self.screen)
