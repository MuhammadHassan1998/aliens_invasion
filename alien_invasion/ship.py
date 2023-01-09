import pygame


class Ship:
    """Player Ship that moves and throw fire"""

    def __init__(self, screen, settings) -> None:
        # ship settings
        self.screen = screen
        # set the settings
        self.settings = settings
        # get the image
        self.image = pygame.image.load("alien_invasion/images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)
        # Moving Flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self) -> None:
        # Draw image on bottom of the screen
        self.screen.blit(self.image, self.rect)

    def update(self) -> None:
        # update the ship movement based upon flags
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.ship_speed_factor
        elif self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.settings.ship_speed_factor
        elif self.moving_up and self.rect.top > self.screen_rect.top:
            self.rect.centery -= self.settings.ship_speed_factor
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += self.settings.ship_speed_factor
        self.rect.centerx = self.center
