import pygame
import sys
from Settings import PageSettings
from Ship import Ship


class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self):

        pygame.init()
        self.pageSetting = PageSettings()
        self.screen = pygame.display.set_mode((self.pageSetting.width, self.pageSetting.height))
        pygame.display.set_caption("Alien Invasion")
        self.my_ship = Ship(self)

    def run_game(self):

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.pageSetting.back_color)
            self.my_ship.blitme()
            pygame.display.flip()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
