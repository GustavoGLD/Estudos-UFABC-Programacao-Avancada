from time import sleep
import pygame
import sys
import random

WIDTH_MAZE = 50
DELAY = 0

class MatrixRenderer:
    def __init__(self, window_size=400, cell_size=100):
        self.window_size = window_size
        self.cell_size = cell_size
        pygame.init()
        self.screen = pygame.display.set_mode((window_size, window_size))
        pygame.display.set_caption("Matrix Renderer")

    def render_matrix(self, matrix):
        if not matrix or not all(isinstance(row, list) for row in matrix):
            raise ValueError("A matriz deve ser uma lista de listas")

        rows = len(matrix)
        cols = len(matrix[0])

        if any(len(row) != cols for row in matrix):
            raise ValueError("Todas as linhas da matriz devem ter o mesmo comprimento")

        cell_width = self.window_size // cols
        cell_height = self.window_size // rows

        self.screen.fill((100, 100, 100))

        for i in range(rows):
            for j in range(cols):
                color = (255, 255, 255) if matrix[i][j] == 1 else (0, 0, 0)
                rect = pygame.Rect(j * cell_width, i * cell_height, cell_width, cell_height)
                pygame.draw.rect(self.screen, color, rect)

        for i in range(1, rows):
            pygame.draw.line(self.screen, (255, 0, 0), (0, i * cell_height), (self.window_size, i * cell_height), 2)

        for j in range(1, cols):
            pygame.draw.line(self.screen, (255, 0, 0), (j * cell_width, 0), (j * cell_width, self.window_size), 2)

        pygame.display.flip()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()
        sys.exit()


def get_neighborhood(matrix, x, y):
    rows = len(matrix)
    cols = len(matrix[0])
    neighborhood = []

    if x > 0:
        neighborhood.append((x - 1, y))
    if x < rows - 1:
        neighborhood.append((x + 1, y))
    if y > 0:
        neighborhood.append((x, y - 1))
    if y < cols - 1:
        neighborhood.append((x, y + 1))

    random.shuffle(neighborhood)

    return neighborhood


def is_point_valid(matrix, x, y):
    white_count = 0
    neighborhood = get_neighborhood(matrix, x, y)

    if matrix[x][y] == 1:
        return False

    for new_x, new_y in neighborhood:
        if matrix[new_x][new_y] == 1:
            white_count += 1

    return white_count <= 1


def backtracking(matrix, init_x=0, init_y=0, renderer=None):
    init_point = (init_x, init_y)
    matrix[init_x][init_y] = 1

    def _backtracking(atual_point):
        pygame.event.pump()  # Processa eventos do pygame para evitar congelamento
        neighborhood = get_neighborhood(matrix, atual_point[0], atual_point[1])

        for neighbor in neighborhood:
            if is_point_valid(matrix, neighbor[0], neighbor[1]):
                matrix[neighbor[0]][neighbor[1]] = 1
                renderer.render_matrix(matrix)
                sleep(DELAY)  # Reduzi o tempo para não demorar muito
                _backtracking(neighbor)

    _backtracking(init_point)


if __name__ == "__main__":
    renderer = MatrixRenderer(window_size=600)
    matrix = [[0] * WIDTH_MAZE for _ in range(WIDTH_MAZE)]
    renderer.render_matrix(matrix)
    backtracking(matrix, renderer=renderer)
    renderer.run()
