from config import *
import pygame


class Node:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.x = MARGIN_SIZE + (row * NODE_SIZE)
        self.y = MARGIN_SIZE + (col * NODE_SIZE)
        self.color = WHITE
        self.valid_neighbors = []

    def update_maze_neighbors(self, grid, visited):
        self.valid_neighbors = []

        if self.row < NUM_COLS - 3 and grid.array[self.row + 2][self.col] not in visited:
            self.valid_neighbors.append(grid.array[self.row + 2][self.col])

        if self.row > 2 and grid.array[self.row - 2][self.col] not in visited:
            self.valid_neighbors.append(grid.array[self.row - 2][self.col])

        if self.col < NUM_ROWS - 3 and grid.array[self.row][self.col + 2] not in visited:
            self.valid_neighbors.append(grid.array[self.row][self.col + 2])

        if self.col > 2 and grid.array[self.row][self.col - 2] not in visited:
            self.valid_neighbors.append(grid.array[self.row][self.col - 2])

    def update_valid_neighbors(self, grid):
        self.valid_neighbors = []

        if self.row < NUM_COLS - 1 and grid.array[self.row + 1][self.col].is_valid():
            self.valid_neighbors.append(grid.array[self.row + 1][self.col])

        if self.row > 0 and grid.array[self.row - 1][self.col].is_valid():
            self.valid_neighbors.append(grid.array[self.row - 1][self.col])

        if self.col < NUM_ROWS - 1 and grid.array[self.row][self.col + 1].is_valid():
            self.valid_neighbors.append(grid.array[self.row][self.col + 1])

        if self.col > 0 and grid.array[self.row][self.col - 1].is_valid():
            self.valid_neighbors.append(grid.array[self.row][self.col - 1])

    # Draws the current Node
    def draw_node(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, NODE_SIZE, NODE_SIZE))

    # Returns the position of the current Node as (x, y)
    # Note: this position represents the top-left corner of the Node
    def get_pos(self):
        return self.x, self.y

    def set_barrier(self):
        self.color = BLACK

    def is_valid(self):
        return not self.is_barrier() and not self.is_visited()

    def is_barrier(self):
        return self.color == BLACK

    def set_start(self):
        self.color = PINK

    def is_start(self):
        return self.color == PINK

    def set_end(self):
        self.color = PURPLE

    def is_end(self):
        return self.color == PURPLE

    def set_checking(self):
        self.color = GREEN

    def is_checking(self):
        return self.color == GREEN

    def set_path(self):
        self.color = BLUE

    def is_path(self):
        return self.color == BLUE

    def set_empty(self):
        self.color = WHITE

    def is_empty(self):
        return self.color == WHITE

    def set_visited(self):
        self.color = RED

    def is_visited(self):
        return self.color == RED