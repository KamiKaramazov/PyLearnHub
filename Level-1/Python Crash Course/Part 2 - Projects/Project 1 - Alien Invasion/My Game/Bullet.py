import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, ai_settings, screen, ship):
        super(Bullet, self).__init__()

        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('Level-1\\Python Crash Course\\Part 2 - Projects\\Project 1 - Alien Invasion\\images\\bullet.bmp')
        self.rect = self.image.get_rect()

        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.speed = ai_settings.bullet_speed
        self.distance = 0

    def update(self):
        self.distance += self.speed
        self.rect.top -= self.speed
        if self.distance >= self.ai_settings.screen_height:
            self.kill()