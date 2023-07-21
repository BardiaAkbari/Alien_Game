class GameStats:

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stat()
        self.high_score = 0

    def reset_stat(self):
        self.ship_left = self.settings.ship_allowed
        self.score = 0
        self.game_level = 1
