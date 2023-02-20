import sys
import pygame
import time
import ctypes
import logging

from Grid import Grid
from constants import *


# TODO: Until the middle mouse button is released, walls affected by starting points/destinations will
#       revert back to walls.

RESOLUTION = (1200, 800)

clock = pygame.time.Clock()
FPS = 60

pygame.init()

class Window:
    def __init__(self):
        # Main window
        pygame.display.set_caption("Pathfinder")
        self.window = pygame.display.set_mode(RESOLUTION, pygame.RESIZABLE)

        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("abc")
        icon = pygame.image.load("resources/icons/32_pathfinder_icon.png").convert()
        pygame.display.set_icon(icon)
        
        # Game variables
        self.running = True
        
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
            if pygame.mouse.get_pressed()[2]:
                mouse_pos = pygame.mouse.get_pos()
                self.grid[min(int(mouse_pos[1]/self.grid.sideLength), len(self.grid)-1)][min(int(mouse_pos[0]/self.grid.sideLength), len(self.grid[0])-1)].setState("Path", self.grid, mouse_pos)
            elif pygame.mouse.get_pressed()[0]:
                # print(pygame.mouse.get_pressed())
                mouse_pos = pygame.mouse.get_pos()
                self.grid[min(int(mouse_pos[1]/self.grid.sideLength), len(self.grid)-1)][min(int(mouse_pos[0]/self.grid.sideLength), len(self.grid[0])-1)].setState("Wall", self.grid, mouse_pos)
            elif pygame.mouse.get_pressed()[1]:
                if not pygame.key.get_pressed()[pygame.K_LCTRL]:
                    mouse_pos = pygame.mouse.get_pos()
                    self.grid[min(int(mouse_pos[1]/self.grid.sideLength), len(self.grid)-1)][min(int(mouse_pos[0]/self.grid.sideLength), len(self.grid[0])-1)].setState("Start", self.grid, mouse_pos)
                else:
                    mouse_pos = pygame.mouse.get_pos()
                    self.grid[min(int(mouse_pos[1]/self.grid.sideLength), len(self.grid)-1)][min(int(mouse_pos[0]/self.grid.sideLength), len(self.grid[0])-1)].setState("Destination", self.grid, mouse_pos)


    # RENDERING
    def Render(self):
        self.window.fill(WHITE)
        self.DrawGrid()
        
    def DrawGrid(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                pygame.draw.rect(self.window, self.grid[i][j].color, self.grid[i][j])
                pygame.draw.rect(self.window, self.grid[i][j].border_color, self.grid[i][j], 1)
    

if __name__ == "__main__":
    Pathfinder = Window()
    Pathfinder.Loop()
    