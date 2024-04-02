class Setting:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        self.ship_speed = 1.5

        self.bullet_speed = 1.0
        self.bullet_width = 10
        self.bullet_height = 30
        self.bullet_color = (255, 255, 255)

        self.ships_left = 3
        self.ship_limit = 3

        self.enemy_speed = 0.5
        self.enemy_drop_rate = 0.12

        self.alien_points = 10

        self.bullets_allowed = 5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 1.0

        self.enemy_speed = 0.5
        self.enemy_drop_rate = 0.12

        self.alien_points = 10

        self.bullets_allowed = 5

    def increase_speed(self):
        self.ship_speed += 0.1
        self.bullet_speed += 0.1
        self.enemy_speed += 0.1
