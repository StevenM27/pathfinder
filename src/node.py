from config import *
import pygame


class Node:
    def __init__(self, row, col):
        self.x = MARGIN_SIZE + (row * NODE_SIZE)
        self.y = MARGIN_SIZE + (col * NODE_SIZE)
        self.color = WHITE

    # Draws the current Node
    def draw_node(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, NODE_SIZE, NODE_SIZE))

    # Returns the position of the current Node as (x, y)
    # Note: this position represents the top-left corner of the Node
    def get_pos(self):
        return self.x, self.y

    def set_barrier(self):
        self.color = BLACK

    def is_barrier(self):
        return self.color == BLACK

    def set_start(self):
        self.color = GREEN

    def is_start(self):
        return self.color == GREEN

    def set_end(self):
        self.color = PURPLE

    def is_end(self):
        return self.color == PURPLE

    def set_empty(self):
        self.color = WHITE

    def is_empty(self):
        return self.color == WHITE
