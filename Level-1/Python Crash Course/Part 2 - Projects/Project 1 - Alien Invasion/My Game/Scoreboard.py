import pygame
from Ship import Ship  # Assuming the Ship class is defined in a separate file named 'ship.py'

class Scoreboard():
    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.ai_settings = ai_settings
        self.stats = stats

        self.font = pygame.font.SysFont(None, 25)

        self.prep_ships()
        self.prep_score()
        self.prep_level()

    def prep_ships(self):
        self.ships = pygame.sprite.Group()
        for i in range(self.stats.ships_left):
            ship_instance = Ship(self.ai_settings, self.screen)  # Create an instance of the Ship class
            ship_instance.rect.x = 10 + (ship_instance.rect.width + 10) * i
            ship_instance.rect.y = 10
            self.ships.add(ship_instance)

    def prep_score(self):
        self.score_image = self.font.render(str(self.stats.score), True, (255, 255, 255))
        self.score_rect = self.score_image.get_rect()
        self.score_rect.centerx = self.screen.get_rect().centerx
        self.score_rect.top = 10

    def prep_level(self):
        self.level_image = self.font.render(str(self.stats.level), True, (255, 255, 255))
        self.level_rect = self.level_image.get_rect()
        self.level_rect.top = 40
        self.level_rect.right = self.screen.get_rect().right - 10

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.level_image, self.level_rect)
