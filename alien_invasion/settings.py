class Settings:
    """Class to store all the settings of the game"""

    def __init__(self) -> None:
        # screen Settings
        self.screen_width = 1200
        self.screen_height = 680
        self.bg_color = (230, 230, 230)
        # ship settings
        self.ship_speed_factor = 1.5
        # bullet settings
        self.bullet_speed = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        # Allien settings
        self.alien_speed_factor = 0.5
        self.fleet_drop_speed = 10
        # 1 means moving to right
        self.fleet_direction = 1
