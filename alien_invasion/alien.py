import logging

import pygame
from pygame.sprite import Sprite


log = logging.getLogger("logger")
log.setLevel(logging.ERROR)


class Alien(Sprite):
    """Player Ship that moves and throw fire"""

    def __init__(self, screen, settings) -> None:
        super().__init__()
        # ship settings
        self.screen = screen
        # set the settings
        self.settings = settings
        # get the image
        try:
            self.image = pygame.image.load("alien_invasion/images/alien.bmp")
        except FileNotFoundError:
            log.error("Can not find the alien image")
            raise FileNotFoundError
        else:
            self.rect = self.image.get_rect()

            # start from the top left
            self.rect.x = self.rect.width
            self.rect.y = self.rect.height

            # alien position
            self.x = float(self.rect.x)

    def blitme(self) -> None:
        self.screen.blit(self.image, self.rect)

    def update(self) -> None:
        # Move the aliens
        self.x += self.settings.alien_speed_factor * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self) -> bool:
        # Check edges
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
