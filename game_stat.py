class GameStats:

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self._reset_stat()

    def _reset_stat(self):
        self.ship_left = self.settings.ship_allowed
