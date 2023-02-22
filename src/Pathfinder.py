import sys
import pygame
import logging

from Window import Window
from AbstractScene import AbstractScene
from Grid import Grid
from BFS import BreadthFirstSearch
from constants import *


class Pathfinder(AbstractScene):
    def __init__(self, window: Window):
        # Grid
        self.grid = Grid(RESOLUTION)
        self.window = window
        self.pygame_window = window.pygame_window

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
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_b]:
            BreadthFirstSearch(self.grid)
        elif keys[pygame.K_ESCAPE]:
            self.window.sceneManager.switchScene(Scenes.Menu)

    # RENDERING
    def Render(self):
        self.pygame_window.fill(WHITE)
        self.DrawGrid()
        
    def DrawGrid(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                pygame.draw.rect(self.pygame_window, self.grid[i][j].color, self.grid[i][j])
                pygame.draw.rect(self.pygame_window, self.grid[i][j].border_color, self.grid[i][j], 1)
