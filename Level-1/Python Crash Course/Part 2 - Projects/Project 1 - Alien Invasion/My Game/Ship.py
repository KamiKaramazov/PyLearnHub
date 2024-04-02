import pygame


class Ship():
    def __init__(self, screen, ai_settings):
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('Level-1\\Python Crash Course\\Part 2 - Projects\\Project 1 - Alien Invasion\\images\\ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()  # Corrected line

        self.center = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed

        self.rect.centerx = self.center
        self.rect.bottom = self.bottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)
