import pygame
from config import *
from node import Node


class Grid:
    def __init__(self):
        self.array = []

        for i in range(NUM_ROWS):
            self.array.append([])
            for j in range(NUM_ROWS):
                self.array[i].append(Node(i, j))

    def draw_grid(self, screen):
        for row in self.array:
            for node in row:
                node.draw_node(screen)

    def draw_lines(self, screen):
        pygame.draw.line(screen, BLACK, (MARGIN_SIZE, MARGIN_SIZE), (MARGIN_SIZE, SCREEN_HEIGHT - MARGIN_SIZE))
        pygame.draw.line(screen, BLACK, (MARGIN_SIZE, MARGIN_SIZE), (SCREEN_WIDTH - MARGIN_SIZE, MARGIN_SIZE))

        for row in self.array:
            for node in row:
                x, y = node.get_pos()

                # Right boundary line
                pygame.draw.line(screen, BLACK, (x + NODE_SIZE, y), (x + NODE_SIZE, y + NODE_SIZE))

                # Bottom boundary line
                pygame.draw.line(screen, BLACK, (x, y + NODE_SIZE), (x + NODE_SIZE, y + NODE_SIZE))

    def draw(self, screen):
        screen.fill(WHITE)

        self.draw_grid(screen)
        self.draw_lines(screen)

        pygame.display.flip()
