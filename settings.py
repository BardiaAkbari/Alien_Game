class Settings:
    """A Class for storing all settings of game"""

    def __init__(self):
        # Game screen Settings
        self.width = 800
        self.height = 600
        self.back_color = (255, 255, 255)
        # Ship Settings
        self.ship_allowed = 3
        # Bullet Settings
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (50, 50, 50)
        self.number_of_allowed_bullet = 40
        # Images URLs
        self.ship_image = "D:\\Final Projects\\OwnProjects\\Alien_Game\\Image\\Ship1.bmp"
        self.alien_image = "D:\\Final Projects\\OwnProjects\\Alien_Game\\Image\\Alien.bmp"
        # Alien Settings
        self.drop_speed = 60
        self.fleet_direction = "Right"
        # Game
        self.game_active = False
        self.game_speed_bonus = 1.2

        self.dynamic_settings()

    def dynamic_settings(self):
        # Ship Settings
        self.ship_speed = 3.0
        # Bullet Settings
        self.bullet_speed = 1.5
        # Alien Settings
        self.alien_speed = 1.0

    def speed_up(self):
        self.ship_speed *= self.game_speed_bonus
        self.bullet_speed *= self.game_speed_bonus
        self.alien_speed *= self.game_speed_bonus
