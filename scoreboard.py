import pygame.font


class Scoreboard:

    def __init__(self, ai_game):

        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.stats = ai_game.stats
        self.settings = ai_game.settings

        self.txt_color = (25, 25, 25)

        self.font = pygame.font.SysFont(None, 40)
        self.render_score()
        self.render_high_score()
        self.render_game_level()

    def render_score(self):
        round_score = round(self.stats.score, -1)
        score_str = "{:,}".format(round_score)
        self.score_image = self.font.render(score_str, True, self.txt_color, self.settings.back_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 10
        self.score_rect.top = 10

    def render_high_score(self):
        round_high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(round_high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.txt_color, self.settings.back_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = 10

    def render_game_level(self):
        game_level_str = str(self.stats.game_level)
        self.game_level_image = self.font.render(game_level_str, True, self.txt_color, self.settings.back_color)
        self.game_level_rect = self.game_level_image.get_rect()
        self.game_level_rect.left = 10
        self.game_level_rect.top = 10

    def draw_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.game_level_image, self.game_level_rect)

    def check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.render_high_score()