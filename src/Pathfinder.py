import sys
import pygame
import time

from Grid import Grid
from constants import *


RESOLUTION = (1200, 800)

clock = pygame.time.Clock()
FPS = 60

pygame.init()

class Window:
    def __init__(self):
        # Main window
        pygame.display.set_caption("Pathfinder")
        self.window = pygame.display.set_mode(RESOLUTION, pygame.RESIZABLE)
        
        # Game variables
        self.running = True
        
        # Player
        # self.player = pygame.Rect(0, 0, 100, 100)
        
        # Grid
        self.grid = Grid(RESOLUTION)

    def Loop(self):
        deltaTime = 0.0
        begin = time.time()
        while self.running:
            deltaTime = time.time() - begin
            begin = time.time()
            
            self.PollInput()
            
            self.Render()
            
            pygame.display.update()
            clock.tick(FPS)

    # INPUTS
    def PollInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                # self.window = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                self.grid = Grid((event.w, event.h))
            if pygame.mouse.get_pressed()[0]:
                # print(pygame.mouse.get_pressed())
                mouse_pos = pygame.mouse.get_pos()
                self.grid[mouse_pos[1]/self.grid.sideLength][mouse_pos[0]/self.grid.sideLength].setState("Wall")
                
    # RENDERING
    def Render(self):
        self.window.fill(WHITE)
        self.DrawGrid()
        
    def DrawGrid(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                pygame.draw.rect(self.window, self.grid[i][j].color, self.grid[i][j], self.grid[i][j].border)
    

if __name__ == "__main__":
    Pathfinder = Window()
    Pathfinder.Loop()
    