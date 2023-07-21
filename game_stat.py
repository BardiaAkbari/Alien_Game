class GameStats:

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stat()

    def reset_stat(self):
        self.ship_left = self.settings.ship_allowed
        self.score = 0
