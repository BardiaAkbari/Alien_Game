import pygame
import sys
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    # Constructor
    def __init__(self):

        pygame.init()
        self.settings = Settings()
        # Display sets
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.width = self.screen.get_rect().width
        self.settings.height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        # Attributes adding
        # Ship
        self.my_ship = Ship(self)
        # Bullet
        self.bullets = pygame.sprite.Group()
        self._number_of_bullet_fires = 0
        # Alien
        self.aliens = pygame.sprite.Group()
        self._creat_alien()

    # Main Function
    def run_game(self):

        while True:
            self._check_events()
            self.my_ship.update_moving()
            self.bullets.update()
            self._delete_not_necessary_bullets()
            self._update_screen()

    # Event Functions
    def _check_events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._keyup_events(event)

    # Key Functions
    def _keydown_events(self, event):

        if event.key == pygame.K_RIGHT:
            self.my_ship.moving_right = True
        if event.key == pygame.K_LEFT:
            self.my_ship.moving_left = True
        if event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _keyup_events(self, event):

        if event.key == pygame.K_RIGHT:
            self.my_ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.my_ship.moving_left = False

    # Screen Functions
    def _update_screen(self):
        self.screen.fill(self.settings.back_color)
        self.my_ship.blitme()
        self._draw_bullets()
        self._draw_aliens()
        pygame.display.flip()

    # Bullet Functions
    def _fire_bullet(self):
        if self._number_of_bullet_fires < self.settings.number_of_allowed_bullet:
            _my_bullet = Bullet(self)
            self.bullets.add(_my_bullet)
            self._number_of_bullet_fires += 1

    def _draw_bullets(self):
        for bullet in self.bullets.sprites():
            bullet.render_bullet()

    def _delete_not_necessary_bullets(self):
        for bullet in self.bullets.copy():
            if bullet.bullet_rect.bottom < 0:
                self.bullets.remove(bullet)

    def _creat_alien(self):
        my_alien = Alien(self)
        self.aliens.add(my_alien)

    def _draw_aliens(self):
        for alien in self.aliens:
            alien.blit_alien()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
