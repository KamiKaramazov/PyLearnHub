import sys
from typing import Self
import pygame
from Settings import Setting
from Bullet import Bullet
from Ship import Ship


class GameFunctions:
    def __init__(self):
        self.ai_settings = Setting()
        self.Bullet = Bullet
        self.Ship = Ship

    def fire_bullet(self, ship):
        if len(self.Bullet) < ship.bullets_allowed:
            new_bullet = self.Bullet(ship.rect.centerx, ship.rect.centery, ship.bullet_speed)
            self.Bullet.add(new_bullet)

    def check_events(self, ship, bullets):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    ship.moving_left = True
                elif event.key == pygame.K_SPACE:
                    self.fire_bullet(ship)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    ship.moving_left = False

    def update_screen(self, ai_settings, screen, ship, bullets):
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()

    def check_collisions(self, ai_settings, screen, ship, bullets, aliens):
        collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
        if collisions:
            ai_settings.increase_score()
        if len(aliens) == 0:
            ai_settings.increase_speed()
            bullets.empty()
            self.create_fleet(ai_settings, screen, ship, aliens)

    def create_fleet(self, ai_settings, screen, ship, aliens):
        alien = self.Ship(ai_settings, screen)
        alien_width, alien_height = alien.rect.width, alien.rect.height
        number_aliens_x = get_number_aliens_x(ai_settings, alien_width)
        number_rows = get_number_rows(ai_settings, ship.rect.height, alien_height)

        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                create_alien(ai_settings, screen, alien_number, row_number, alien_width, alien_height, aliens)

    def check_fleet_edges(self, ai_settings, aliens):
        for alien in aliens.sprites():
            if alien.check_edges():
                change_fleet_direction(ai_settings, aliens)
                break

    def update_fleets(self, ai_settings, screen, stats, ship, aliens, bullets):
        if len(aliens) > 0:
            self.check_fleet_edges(ai_settings, aliens)
            aliens.update()
            if pygame.sprite.spritecollideany(ship, aliens):
                ship_hit(ai_settings, stats, screen, ship, aliens, bullets)

            for alien in aliens:
                if alien.rect.bottom >= screen.get_rect().bottom:
                    ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
                    break

def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = (ai_settings.screen_height -
                         (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_settings, screen, alien_number, row_number, alien_width, alien_height, aliens):
    alien = Self.Ship(ai_settings, screen)
    alien_width, alien_height = alien.rect.width, alien.rect.height
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    stats.ships_left -= 1
    stats.reset_stats()
    bullets.empty()
    aliens.empty()
    ship.center_ship()
    ai_settings.initialize_dynamic_settings()