import pygame
import sys
from Settings import PageSettings
from Ship import Ship


class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self):

        pygame.init()
        self.settings = PageSettings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.width = self.screen.get_rect().width
        self.settings.height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        self.my_ship = Ship(self)

    def run_game(self):

        while True:
            self._check_events()
            self.my_ship.update_moving()
            self._update_screen()

    def _check_events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._keyup_events(event)

    def _keydown_events(self, event):

        if event.key == pygame.K_RIGHT:
            self.my_ship.moving_right = True
        if event.key == pygame.K_LEFT:
            self.my_ship.moving_left = True
        if event.key == pygame.K_q:
            sys.exit()

    def _keyup_events(self, event):

        if event.key == pygame.K_RIGHT:
            self.my_ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.my_ship.moving_left = False

    def _update_screen(self):
        self.screen.fill(self.settings.back_color)
        self.my_ship.blitme()
        pygame.display.flip()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
