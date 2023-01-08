import sys

import pygame


def run_game():
    """Main Function where the game starts"""

    pygame.init()
    screen = pygame.display.set_mode((1200, 700))
    pygame.display.set_caption("Alien Invasion")

    # Main Loop of the game
    while True:
        # watch for keyboard event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Make the recent screen visible
        pygame.display.flip()


run_game()
