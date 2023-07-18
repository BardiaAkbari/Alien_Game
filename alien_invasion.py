import pygame
import sys
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from time import sleep
from game_stat import GameStats


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
        # Game Stats
        self.stats = GameStats(self)
        # Bullet
        self.bullets = pygame.sprite.Group()
        self._number_of_bullet_fires = 0
        # Alien
        self.aliens = pygame.sprite.Group()
        self._creat_fleet()

    # Main Function
    def run_game(self):

        while True:
            self._check_events()
            if self.settings.game_active:
                self.my_ship.update_moving()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()

    # Screen Functions
    def _update_screen(self):
        self.screen.fill(self.settings.back_color)
        self.my_ship.blitme()
        self._draw_bullets()
        self._draw_aliens()
        pygame.display.flip()

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
            if self.settings.game_active:
                self._fire_bullet()

    def _keyup_events(self, event):

        if event.key == pygame.K_RIGHT:
            self.my_ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.my_ship.moving_left = False

    # Bullet Functions
    def _fire_bullet(self):
        if self._number_of_bullet_fires < self.settings.number_of_allowed_bullet:
            _my_bullet = Bullet(self)
            self.bullets.add(_my_bullet)
            self._number_of_bullet_fires += 1

    def _draw_bullets(self):
        for bullet in self.bullets.sprites():
            bullet.render_bullet()

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)
        self._managing_collisions()

    def _managing_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if len(self.aliens) == 0:
            self._creat_fleet()
            self.bullets.empty()
            self._number_of_bullet_fires = 0

    # Alien Functions
    def _creat_fleet(self):
        alien_sample = Alien(self)
        alien_width = alien_sample.rect.width
        alien_height = alien_sample.rect.height
        available_alien_space_by_x = self.settings.width - 2 * alien_width
        number_of_alien_by_x = available_alien_space_by_x // (2 * alien_width)
        for alien_num in range(number_of_alien_by_x):
            for column in range(3):
                my_alien = Alien(self)
                my_alien.alien_x_position = alien_width + 2 * alien_num * alien_width
                my_alien.rect.x = my_alien.alien_x_position
                my_alien.alien_y_position = alien_height + 2 * column * 56
                my_alien.rect.y = my_alien.alien_y_position
                self.aliens.add(my_alien)

    def _update_aliens(self):
        self._check_direction()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.my_ship, self.aliens):
            self._reset_game()
        self._check_alien_pass()

    def _reset_game(self):

        if self.stats.ship_left > 0:

            self.stats.ship_left -= 1
            self.my_ship.reset_ship()
            self.bullets.empty()
            self._number_of_bullet_fires = 0
            self.aliens.empty()
            self._creat_fleet()
            sleep(1.0)
        else:
            self.settings.game_active = False

    def _check_alien_pass(self):
        for alien in self.aliens:
            if alien.rect.bottom >= self.screen.get_rect().bottom:
                self._reset_game()
                break

    def _check_direction(self):

        for alien in self.aliens:
            if alien.rect.right >= self.screen.get_rect().right:
                self.settings.fleet_direction = "Left"
                self._alien_dropping()
                break
            if alien.rect.left <= 0:
                self.settings.fleet_direction = "Right"
                self._alien_dropping()
                break

    def _alien_dropping(self):

        for alien in self.aliens:
            alien.rect.y += self.settings.drop_speed

    def _draw_aliens(self):
        for alien in self.aliens:
            alien.blit_alien()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
