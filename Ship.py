import pygame


class Ship:

    def __init__(self, ai_game):
        self.gameScreen = ai_game.screen
        self.gameScreen_rect = ai_game.screen.get_rect()
        self.ship_image = pygame.image.load("D:\\Final Projects\\OwnProjects\\Alien_Game\\Image\\Ship1.bmp")
        self.ship_image_rect = self.ship_image.get_rect()

        self.ship_image_rect.midbottom = self.gameScreen_rect.midbottom

    def blitme(self):

        self.gameScreen.blit(self.ship_image, self.ship_image_rect)

