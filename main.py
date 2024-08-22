import pygame
from constants import *

def main():
    # Initialize Pygame
    pygame.init()

    # Print statements
    print("Starting asteroids!")
    print("Screen width: {}".format(SCREEN_WIDTH))
    print("Screen height: {}".format(SCREEN_HEIGHT))

    # Create the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Game loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # Fill the screen with black color
        screen.fill((0, 0, 0))

        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()