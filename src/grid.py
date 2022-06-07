import pygame
from config import *
from node import Node
from queue import PriorityQueue
import random


class Grid:
    def __init__(self):
        self.array = []

        for i in range(NUM_COLS):
            self.array.append([])
            for j in range(NUM_ROWS):
                self.array[i].append(Node(i, j))

    def draw_grid(self, screen):
        for row in self.array:
            for node in row:
                node.draw_node(screen)

    def draw_lines(self, screen):
        pygame.draw.line(screen, GRAY, (MARGIN_SIZE, MARGIN_SIZE), (MARGIN_SIZE, SCREEN_HEIGHT - MARGIN_SIZE))
        pygame.draw.line(screen, GRAY, (MARGIN_SIZE, MARGIN_SIZE), (SCREEN_WIDTH - MARGIN_SIZE, MARGIN_SIZE))

        for row in self.array:
            for node in row:
                x, y = node.get_pos()

                # Right boundary line
                pygame.draw.line(screen, GRAY, (x + NODE_SIZE, y), (x + NODE_SIZE, y + NODE_SIZE))

                # Bottom boundary line
                pygame.draw.line(screen, GRAY, (x, y + NODE_SIZE), (x + NODE_SIZE, y + NODE_SIZE))

    def draw(self, screen):
        screen.fill(WHITE)

        self.draw_grid(screen)
        self.draw_lines(screen)

        pygame.display.flip()

    def break_wall(self, a, b):
        target_row = (a.row + b.row) // 2
        target_col = (a.col + b.col) // 2

        self.array[target_row][target_col].set_empty()

    def generate_maze(self):

        # Build maze walls
        for row in self.array:
            for node in row:
                if node.col == 0 or node.col == NUM_COLS - 1 or node.row == 0 or node.row == NUM_ROWS - 1:
                    node.set_barrier()
                if node.row % 2 == 0 or node.col % 2 == 0:
                    node.set_barrier()

        # Tear down walls to make maze
        current = self.array[1][1]
        count = 0
        stack = PriorityQueue()
        stack.put((count, current))
        visited = {current}

        while not stack.empty():
            current = stack.get()[1]
            current.update_maze_neighbors(self, visited)

            if len(current.valid_neighbors) != 0:
                count -= 1
                stack.put((count, current))

                rand = random.randint(0, len(current.valid_neighbors) - 1)
                chosen = current.valid_neighbors[rand]

                self.break_wall(current, chosen)
                visited.add(chosen)
                count -= 1
                stack.put((count, chosen))
