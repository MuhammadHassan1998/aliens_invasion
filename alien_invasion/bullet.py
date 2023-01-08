import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Bullet Class"""

    def __init__(self, settings, screen, ship) -> None:
        # initializes bullet
        super().__init__()
        self.screen = screen
        # creating bullet at 0 0 first
        self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # bullet position
        self.y = float(self.rect.y)
        self.color = settings.bullet_color
        self.speed = settings.bullet_speed

    def draw_bullet(self) -> None:
        # draw the bullet on the screen
        pygame.draw.rect(self.screen, self.color, self.rect)

    def update(self) -> None:
        # Move bullet up the screen
        self.y -= self.speed
        self.rect.y = self.y
