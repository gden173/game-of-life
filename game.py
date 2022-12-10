"""
Short pygame implementation of Conways Game of Life 
"""

import pygame
import time
import copy


GRID_WIDTH = 20
GRID_HEIGHT = 20
CELL_SIZE = 50

# Define the colors for the game grid and cells
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create a 2D array to store the state of each cell in the game grid
empty_grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
grid = copy.deepcopy(empty_grid)

# Initialize Pygame and create a window
pygame.init()
window = pygame.display.set_mode((GRID_WIDTH * CELL_SIZE, GRID_HEIGHT * CELL_SIZE))

# Initialize the state of the cells in the game grid
# Blinker
grid[9][10] = 1
grid[10][10] = 1
grid[11][10] = 1


def draw_rect(x, y):
    pygame.draw.rect(
        window, BLACK, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    )


def update_board():
    global grid
    global window
    window.fill(WHITE)
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            if grid[x][y] == 1:
                draw_rect(x, y)
    pygame.display.update()


while True:
    update_board()
    next_grid = copy.deepcopy(empty_grid)
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            v = sum(
                [
                    grid[j][k]
                    for j in range(max(x - 1, 0), min(x + 2, GRID_WIDTH))
                    for k in range(max(y - 1, 0), min(y + 2, GRID_HEIGHT))
                    if not (j == x and k == y)
                ]
            )

            if grid[x][y] == 1:
                next_grid[x][y] = int(v in [2, 3])
            if v == 3:
                next_grid[x][y] = 1

    # Handle user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Clear the screen and draw the game grid and cells
    time.sleep(0.3)
    update_board()
    grid = copy.deepcopy(next_grid)
