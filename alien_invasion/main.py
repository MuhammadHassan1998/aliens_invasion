import logging

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf


log = logging.getLogger("logger")
log.setLevel(logging.ERROR)


def run_game():
    """Main Function where the game starts"""

    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode(
        (game_settings.screen_width, game_settings.screen_height)
    )

    # Bullets
    bullets = Group()
    aliens = Group()

    # get the ship and aliens
    try:
        ship = Ship(screen=screen, settings=game_settings)
        gf.create_fleet(settings=game_settings, screen=screen, ship=ship, aliens=aliens)
    except FileNotFoundError:
        log.error("Can not find the image")
        return

    pygame.display.set_caption("Alien Invasion")

    # Main Loop of the game
    while True:
        gf.check_event(
            ship=ship, screen=screen, bullets=bullets, settings=game_settings
        )
        ship.update()
        bullets.update()
        gf.update_screen(
            settings=game_settings,
            screen=screen,
            ship=ship,
            bullets=bullets,
            aliens=aliens,
        )
        gf.update_bullets(
            settings=game_settings,
            screen=screen,
            ship=ship,
            bullets=bullets,
            aliens=aliens,
        )
        gf.update_aliens(settings=game_settings, aliens=aliens)


run_game()
