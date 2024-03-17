import sys
import pygame
from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True  # If right arrow key is pressed, move the ship right
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True  # If left arrow key is pressed, move the ship left
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)  # If spacebar is pressed, fire a bullet

def check_keyup_events(event, ship):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False  # If right arrow key is released, stop moving the ship right
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False  # If left arrow key is released, stop moving the ship left

def check_events(ai_settings, screen, ship, bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()  # If the 'X' button is clicked, exit the game
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)  # Check keydown events
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)  # Check keyup events

def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet if limit not reached yet."""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)  # Create a new bullet object
        bullets.add(new_bullet)  # Add the new bullet to the bullets group

def update_screen(ai_settings, screen, ship, bullets):
    """Update images on the screen and flip to the new screen."""
    screen.fill(ai_settings.bg_color)  # Fill the background with the specified color

    # Redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()  # Draw each bullet on the screen
    ship.blitme()  # Draw the ship on the screen

    pygame.display.flip()  # Make the most recently drawn screen visible

def update_bullets(bullets):
    """Update position of bullets and get rid of old bullets."""
    bullets.update()  # Update the position of all bullets

    # Get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)  # Remove the bullet from the bullets group if it goes off the screen
