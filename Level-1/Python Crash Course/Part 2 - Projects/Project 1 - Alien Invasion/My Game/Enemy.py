import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, ai_settings, screen):
        super(Enemy, self).__init__()

        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('Level-1\\Python Crash Course\\Part 2 - Projects\\Project 1 - Alien Invasion\\images\\alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.speed = ai_settings.enemy_speed
        self.direction = pygame.Vector2(1, 0)

    def update(self):
        self.rect.x += self.speed * self.direction.x
        self.rect.y += self.speed * self.direction.y

        if self.rect.right >= self.screen_rect.right:
            self.direction.x = -1
        if self.rect.left <= 0:
            self.direction.x = 1