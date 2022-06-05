import pygame
from pygame.locals import *

# Local modules
from config import *
from grid import Grid
from search import *

# Initialize pygame display
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

grid = Grid()
running = True

start = None
end = None

started = False

# Game loop
while running:

    # Draw the screen on every frame
    grid.draw(screen)

    # Look at every event in the queue
    for event in pygame.event.get():

        # User clicked a key
        if event.type == KEYDOWN:

            # User clicked the "D" key
            if event.key == K_d and not started:
                if start and end:
                    # Dijkstra's algorithm
                    started = True
                    dijkstra(start, end, grid, screen, pygame)
                else:
                    pass
                started = False

            # reset grid
            if event.key == K_r and not started:
                grid = Grid()
                start = None
                end = None

            # User clicked the ESCAPE key, closing the game
            if event.key == K_ESCAPE:
                running = False

        # Left mouse click
        if pygame.mouse.get_pressed(3)[0]:
            x, y = pygame.mouse.get_pos()
            i = (x - MARGIN_SIZE) // NODE_SIZE
            j = (y - MARGIN_SIZE) // NODE_SIZE

            if i < 0 or i >= len(grid.array[0]) or j < 0 or j >= len(grid.array[0]):
                continue

            node = grid.array[i][j]

            if not start and node.is_empty():
                start = node
                start.set_start()

            elif not end and node.is_empty():
                end = node
                end.set_end()

            elif end != node and start != node:
                node.set_barrier()

        # Right mouse click
        if pygame.mouse.get_pressed(3)[2]:
            x, y = pygame.mouse.get_pos()
            i = (x - MARGIN_SIZE) // NODE_SIZE
            j = (y - MARGIN_SIZE) // NODE_SIZE

            if i < 0 or i >= len(grid.array[0]) or j < 0 or j >= len(grid.array[0]):
                continue

            node = grid.array[i][j]

            if node == start:
                start = None
                node.set_empty()
            elif node == end:
                end = None
                node.set_empty()
            else:
                node.set_empty()

        # User clicked close window button
        if event.type == QUIT:
            running = False
