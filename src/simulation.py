import pygame

CELL_SIZE = 20
ROWS = 25
COLS = 25

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
GRAY = (200,200,200)

def draw_grid(screen, grid, path, goal):
    for i in range(ROWS):
        for j in range(COLS):

            color = WHITE

            if grid[i][j] == 1:
                color = BLACK

            if (i,j) in path:
                color = BLUE

            pygame.draw.rect(screen, color,
                             (j*CELL_SIZE, i*CELL_SIZE, CELL_SIZE, CELL_SIZE))

            pygame.draw.rect(screen, GRAY,
                             (j*CELL_SIZE, i*CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

    # draw goal
    pygame.draw.rect(screen, RED,
                     (goal[1]*CELL_SIZE, goal[0]*CELL_SIZE, CELL_SIZE, CELL_SIZE))


def draw_robot(screen, pos):
    pygame.draw.circle(
        screen,
        GREEN,
        (
            pos[1]*CELL_SIZE + CELL_SIZE//2,
            pos[0]*CELL_SIZE + CELL_SIZE//2
        ),
        CELL_SIZE//3
    )
