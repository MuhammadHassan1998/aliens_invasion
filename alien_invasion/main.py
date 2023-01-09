import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    """Main Function where the game starts"""

    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode(
        (game_settings.screen_width, game_settings.screen_height)
    )
    # get the ship
    try:
        ship = Ship(screen=screen, settings=game_settings)
    except FileNotFoundError:
        return

    pygame.display.set_caption("Alien Invasion")

    # Bullets
    bullets = Group()

    # Main Loop of the game
    while True:
        gf.check_event(
            ship=ship, screen=screen, bullets=bullets, settings=game_settings
        )
        ship.update()
        bullets.update()
        gf.update_screen(
            settings=game_settings, screen=screen, ship=ship, bullets=bullets
        )
        gf.update_bullets(bullets=bullets)


run_game()
