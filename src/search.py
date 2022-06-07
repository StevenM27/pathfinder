from queue import PriorityQueue
from config import *


def h(a, b):
    return abs(a.row - b.row) + abs(a.col - b.col)


def a_star(start, end, grid, screen, pg):
    node_id = 0
    node_queue = PriorityQueue()
    node_hash = {start}
    node_queue.put((0, node_id, start))
    came_from = {}
    g_score = {node: float("inf") for row in grid.array for node in row}
    g_score[start] = 0
    f_score = {node: float("inf") for row in grid.array for node in row}
    f_score[start] = h(start, end)

    while not node_queue.empty():
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

        current = node_queue.get()[2]
        node_hash.remove(current)

        if current == end:
            while current != start:
                current = came_from[current]
                if current != start and current != end:
                    current.set_path()
                    grid.draw(screen)
            return

        current.update_valid_neighbors(grid)

        for node in current.valid_neighbors:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[node]:
                came_from[node] = current
                g_score[node] = temp_g_score
                f_score[node] = temp_g_score + h(node, end)

                if node not in node_hash:
                    node_id += 1
                    node_queue.put((f_score[node], node_id, node))
                    node_hash.add(node)
                    if node != end:
                        node.set_checking()

            grid.draw(screen)

            if current != start:
                current.set_visited()


def dijkstra(start, end, grid, screen, pg):
    node_id = 0
    node_queue = PriorityQueue()
    node_hash = {start}
    node_queue.put((0, node_id, start))
    came_from = {}
    distance = {node: float("inf") for row in grid.array for node in row}
    distance[start] = 0

    while not node_queue.empty():
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

        current = node_queue.get()[2]
        node_hash.remove(current)

        if current == end:
            while current != start:
                current = came_from[current]
                if current != start and current != end:
                    current.set_path()
                    grid.draw(screen)
            return

        current.update_valid_neighbors(grid)

        for node in current.valid_neighbors:
            temp_distance = distance[current] + 1

            if temp_distance < distance[node]:
                came_from[node] = current
                distance[node] = temp_distance

                if node not in node_hash:
                    node_id += 1
                    node_queue.put((distance[node], node_id, node))
                    node_hash.add(node)
                    if node != end:
                        node.set_checking()

        grid.draw(screen)

        if current != start:
            current.set_visited()
