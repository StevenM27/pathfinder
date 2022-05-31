import pygame
from pygame.locals import *

# Local modules
from config import *
from grid import Grid

# Initialize pygame display
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

grid = Grid()
running = True

# Game loop
while running:

    # Draw the screen on every frame
    grid.draw(screen)

    # Look at every event in the queue
    for event in pygame.event.get():

        # User clicked a key
        if event.type == KEYDOWN:

            # User clicked the ESCAPE key, closing the game
            if event.key == K_ESCAPE:
                running = False

        # User clicked close window button
        elif event.type == QUIT:
            running = False
