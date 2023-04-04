class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game settings."""

        # Screen settings
        self.screen_width = 600
        self.screen_height = 400
        self.bg_color = (147, 215, 231)

        # Ship's settings
        self.ship_speed = 1

        # Bullet settings
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3