import sys

import pygame

from bullet import Bullet


def left_right_up_down_movement(ship, event, is_down=False) -> None:
    # Moves the ship to left and right
    if event.key == pygame.K_RIGHT:
        ship.moving_right = is_down
    elif event.key == pygame.K_LEFT:
        ship.moving_left = is_down
    elif event.key == pygame.K_UP:
        ship.moving_up = is_down
    elif event.key == pygame.K_DOWN:
        ship.moving_down = is_down


def fire_bullet(settings, screen, ship, bullets):
    # fires the bullets
    new_bullet = Bullet(settings=settings, screen=screen, ship=ship)
    bullets.add(new_bullet)


def check_event(ship, screen, bullets, settings) -> None:
    # watch for keyboard event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and len(bullets) < settings.bullets_allowed:
                fire_bullet(
                    settings=settings, screen=screen, ship=ship, bullets=bullets
                )
            else:
                left_right_up_down_movement(ship=ship, event=event, is_down=True)

        elif event.type == pygame.KEYUP:
            left_right_up_down_movement(ship=ship, event=event)


def update_screen(settings, screen, ship, bullets) -> None:
    # updates the screen every time
    screen.fill(settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    # Make the recent screen visible
    pygame.display.flip()


def update_bullets(bullets):
    # remove the unused bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
