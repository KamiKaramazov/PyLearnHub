import pygame


class Button():
    def __init__(self, screen, msg, x, y, w, h, ic, ac, action=None):
        self.screen = screen
        self.msg = msg
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.ic = ic
        self.ac = ac
        self.action = action

        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.image = pygame.Surface((self.w, self.h))

    def draw(self):
        self.image.fill(self.ic)
        pygame.draw.rect(self.image, self.ac, self.rect, 2)
        self.screen.blit(self.image, (self.x, self.y))
        font = pygame.font.SysFont(None, 30)
        text = font.render(self.msg, True, (0, 0, 0))
        self.screen.blit(text, (self.x + (self.w / 2) - (text.get_width() / 2), self.y + (self.h / 2) - (text.get_height() / 2)))

    def check_for_input(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            if self.action:
                self.action()