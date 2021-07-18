import numpy as np
import pygame
from collections import deque 

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (55,118,171)
screen = pygame.display.set_mode([800,800])
WIDTH = 20
HEIGHT = 20
MARGIN = 1
pygame.init()
grid = np.zeros((38,38))
grid[5][5] = 1
grid[30][30] = 1
clock = pygame.time.Clock()

def draw():
    for row in range(38):
        for column in range(38):
            color = BLACK
            if grid[row][column] == 1:
                color = GREEN
            if grid[row][column] == 2:
                color = WHITE
            
            if grid[row][column] == 3:
                color = BLUE
                
            if grid[row][column] == 4:
                color = WHITE
            
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])

def main():
    screen.fill(RED)
    done = False
    queue = []
    queue.append([5,5])
    visited = []
    visited.append([5,5])
    path = []
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 2:
                    done = True
                    break
            if event.type == pygame.QUIT:  
                done = True 
            if pygame.mouse.get_pressed()[0]:
                try:
                    pos = event.pos
                    column = pos[0] // (WIDTH + MARGIN)
                    row = pos[1] // (HEIGHT + MARGIN)
                    grid[row][column] = 2
                except IndexError:
                    pass
                except AttributeError:
                    pass
        draw()
        clock.tick(60)
        pygame.display.flip()
        
    
    N, M = 38, 38
    directions = [[0,1], [1,0], [0,-1], [-1,0]]
    q = deque()
    q.append([5,5,0])
    visited = set()
    path = []
    
    while len(q) > 0:
        cr, cc, cdist = q.popleft()
        if cr == 30 and cc == 30:
            return cdist
        
        if grid[cr][cc] == 2:
            continue
        
        for direction in directions:
            
            nr, nc = cr + direction[0], cc + direction[1]
            if 0 <= nr < N and 0 <= nc < M and (nr,nc) not in visited:
                q.append([nr, nc, cdist + 1])
                visited.add((nr, nc))
                              
    pygame.quit()


