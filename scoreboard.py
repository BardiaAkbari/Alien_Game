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

    def render_score(self):
        round_score = round(self.stats.score, -1)
        score_str = "{:,}".format(round_score)
        self.score_image = self.font.render(score_str, True, self.txt_color, self.settings.back_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 10
        self.score_rect.top = 10

    def draw_score(self):
        self.screen.blit(self.score_image, self.score_rect)