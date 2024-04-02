import sys
import pygame

from Settings import Setting
from Ship import Ship
from Game_Stats import GameStats
from Scoreboard import Scoreboard
from Button import Button
from Game_Functions import GameFunctions as gf



def run_game():
    pygame.init()
    ai_settings = Setting()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    ship = Ship(screen, ai_settings)
    bullets = pygame.sprite.Group()
    enemies = pygame.sprite.Group()

    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    play_button = Button(screen, 'Play', 350, 300, 100, 50, (102, 205, 170), (255, 255, 255), run_game)

    clock = pygame.time.Clock()

    while True:
        clock.tick(60)

        if stats.ships_left > 0:
            gf.check_events(ai_settings, screen, ship, bullets, stats, play_button)
            if stats.game_active:
                ship.update()
                gf.update_bullets(bullets, enemies, ai_settings, screen, stats)
                gf.update_enemies(ai_settings, enemies, stats)
            gf.update_screen(ai_settings, screen, ship, bullets, enemies, stats, sb)
        else:
            play_button.draw()
            pygame.display.flip()

            while True:
                clock.tick(60)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        play_button.check_for_input(mouse_pos)

if __name__ == '__main__':
    run_game()