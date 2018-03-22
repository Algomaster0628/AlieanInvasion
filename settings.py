class Settings():
    """A class to store all settings for Alian Invasion"""

    def __init__(self):
        """Initialize the game's static settings"""
        #screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230,230,230)

        # Ship Settings
        self.ship_limit = 3

        # Bullet settings.
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed =  3

        # Alien Settings
        self.fleet_drop_speed = 7

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        # How quickly the alien point value increase.
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 1.1
        self.bullet_speed_factor = .8
        self.alien_speed_factor = .4

        # fleet_direction of 1 represents right and -1 represents left\
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien value points"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        
