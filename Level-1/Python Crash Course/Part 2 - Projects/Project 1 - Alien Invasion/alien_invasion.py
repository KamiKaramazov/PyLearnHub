import pygame
from pygame.sprite import Group

# Import custom classes and modules
from settings import Settings  # Import the Settings class from settings.py
from ship import Ship          # Import the Ship class from ship.py
import game_functions as gf   # Import the game_functions module as gf

def run_game():
    # Initialize pygame
    pygame.init()
    
    # Create a Settings object to store game settings
    ai_settings = Settings()  # Instantiate a Settings object
    
    # Create a display window with the specified dimensions
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    
    # Set the title of the display window
    pygame.display.set_caption("Alien Invasion")
    
    # Set the background color
    bg_color = (0, 10, 150)
    
    # Create a Ship object
    ship = Ship(ai_settings, screen)  # Instantiate a Ship object
    
    # Create a Group to store bullets
    bullets = Group()  # Create a Group to hold bullet instances

    # Main game loop
    while True:
        # Check for and handle events (e.g., keyboard/mouse input)
        gf.check_events(ai_settings, screen, ship, bullets)  # Call the check_events function
        
        # Update the ship's position
        ship.update()  # Call the update method of the Ship object
        
        # Update the position of bullets and remove old bullets
        gf.update_bullets(bullets)  # Call the update_bullets function
        
        # Update the display to reflect changes
        gf.update_screen(ai_settings, screen, ship, bullets)  # Call the update_screen function

# Run the game
run_game()
