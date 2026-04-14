import pygame
import random
import time
from simulation import *
from path_planning import astar

pygame.init()

screen = pygame.display.set_mode((COLS*CELL_SIZE, ROWS*CELL_SIZE))
pygame.display.set_caption("Autonomous Navigation - Realistic")

grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]

# initial obstacles
for _ in range(100):
    x = random.randint(0, ROWS-1)
    y = random.randint(0, COLS-1)
    if (x, y) != (0,0) and (x, y) != (24,24):
        grid[x][y] = 1

start = (0,0)
goal = (24,24)

robot_pos = start
path = astar(grid, robot_pos, goal)

running = True
step_index = 0
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)

    # occasionally add dynamic obstacle
    if random.random() < 0.02:
        ox = random.randint(0, ROWS-1)
        oy = random.randint(0, COLS-1)
        if (ox, oy) != robot_pos and (ox, oy) != goal:
            grid[ox][oy] = 1

    # if path blocked → replan
    if step_index < len(path):
        next_step = path[step_index]
        if grid[next_step[0]][next_step[1]] == 1:
            path = astar(grid, robot_pos, goal)
            step_index = 0

    # move robot
    if step_index < len(path):
        robot_pos = path[step_index]
        step_index += 1

    draw_grid(screen, grid, path, goal)
    draw_robot(screen, robot_pos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(10)  # controls speed

pygame.quit()