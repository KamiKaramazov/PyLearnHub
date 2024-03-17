class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings.
        self.screen_width = 1200  # Width of the game window
        self.screen_height = 700  # Height of the game window
        self.bg_color = (0, 1, 131)  # Background color of the game window

        # Ship settings.
        self.ship_speed_factor = 1  # Speed of the ship's movement

        # Bullet settings.
        self.bullet_speed_factor = 1  # Speed of the bullet's movement
        self.bullet_width = 3  # Width of the bullet
        self.bullet_height = 15  # Height of the bullet
        self.bullet_color = (255, 13, 24)  # Color of the bullet
        self.bullets_allowed = 3  # Maximum number of bullets allowed on screen
