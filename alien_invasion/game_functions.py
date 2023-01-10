import sys

import pygame

from bullet import Bullet
from alien import Alien


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


def update_screen(settings, screen, ship, bullets, aliens) -> None:
    # updates the screen every time
    screen.fill(settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    aliens.draw(screen)
    ship.blitme()
    # Make the recent screen visible
    pygame.display.flip()


def update_bullets(settings, screen, ship, bullets, aliens) -> None:
    # remove the unused bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        bullets.empty()
        settings.alien_speed_factor += 0.1
        create_fleet(settings=settings, screen=screen, ship=ship, aliens=aliens)


def get_alien_number(settings, alien_width) -> int:
    # Get the number of aliens in a row
    available_space_x = settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(settings, ship_height, alien_height) -> int:
    # return number of rows available for aliens
    available_space_y = settings.screen_height - (3 * alien_height) - ship_height
    number_of_rows = int(available_space_y / (2 * alien_height))
    return number_of_rows


def create_alien(settings, screen, aliens, alien_number, row_number) -> None:
    # Create row of aliens
    alien = Alien(screen=screen, settings=settings)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(screen, settings, ship, aliens) -> None:
    # creating fleet of aliens
    alien = Alien(screen=screen, settings=settings)
    alien_number_x = get_alien_number(settings=settings, alien_width=alien.rect.width)
    rows = get_number_rows(
        settings=settings, ship_height=ship.rect.height, alien_height=alien.rect.height
    )
    for row_number in range(rows):
        for alien_number in range(alien_number_x):
            create_alien(
                settings=settings,
                screen=screen,
                aliens=aliens,
                alien_number=alien_number,
                row_number=row_number,
            )


def change_fleet_direction(settings, aliens) -> None:
    for alien in aliens.sprites():
        alien.rect.y += settings.fleet_drop_speed
    settings.fleet_direction *= -1


def check_fleet_edges(settings, aliens) -> None:
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(settings=settings, aliens=aliens)
            break


def update_aliens(settings, aliens) -> None:
    # Update the position of aliens
    check_fleet_edges(settings=settings, aliens=aliens)
    aliens.update()
