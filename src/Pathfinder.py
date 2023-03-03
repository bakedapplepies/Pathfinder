import pygame
import sys

from Window import Window
from AbstractScene import AbstractScene
from Grid import Grid
from BFS import BreadthFirstSearch
from Dijkstra import Dijkstra
from constants import *


class Pathfinder(AbstractScene):
    def __init__(self, window: Window):
        # window
        self.window = window
        self.pygame_window = window.pygame_window
        
        # Grid
        self.grid = Grid(RESOLUTION)

    # INPUTS
    def PollInput(self):
        keydown = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                # self.window = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                self.grid = Grid((event.w, event.h))
            if event.type == pygame.KEYDOWN:
                keydown = True
            if pygame.mouse.get_pressed()[2]:
                mouse_pos = pygame.mouse.get_pos()
                self.grid[min(int(mouse_pos[1]/self.grid.sideLength), len(self.grid)-1)][min(int(mouse_pos[0]/self.grid.sideLength), len(self.grid[0])-1)].setState(NodeState.PATH, self.grid, mouse_pos)
            elif pygame.mouse.get_pressed()[0]:
                # print(pygame.mouse.get_pressed())
                mouse_pos = pygame.mouse.get_pos()
                self.grid[min(int(mouse_pos[1]/self.grid.sideLength), len(self.grid)-1)][min(int(mouse_pos[0]/self.grid.sideLength), len(self.grid[0])-1)].setState(NodeState.WALL, self.grid, mouse_pos)
            elif pygame.mouse.get_pressed()[1]:
                if not pygame.key.get_pressed()[pygame.K_LCTRL]:
                    mouse_pos = pygame.mouse.get_pos()
                    self.grid[min(int(mouse_pos[1]/self.grid.sideLength), len(self.grid)-1)][min(int(mouse_pos[0]/self.grid.sideLength), len(self.grid[0])-1)].setState(NodeState.START, self.grid, mouse_pos)
                else:
                    mouse_pos = pygame.mouse.get_pos()
                    self.grid[min(int(mouse_pos[1]/self.grid.sideLength), len(self.grid)-1)][min(int(mouse_pos[0]/self.grid.sideLength), len(self.grid[0])-1)].setState(NodeState.DESTINATION, self.grid, mouse_pos)
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_b] and keydown and self.grid.rowStart != None and self.grid.rowDestination != None:
            print("Started Pathfinding.")
            # BreadthFirstSearch(self.grid, self.window)
            Dijkstra(self.grid, self.window)
        elif keys[pygame.K_ESCAPE] and keydown:  # Menu
            self.window.paused = True
            self.window.sceneManager.switchScene(Scenes.MENU)
        elif keys[pygame.K_g] and keydown:  # New Grid
            self.grid = Grid(RESOLUTION)

    # RENDERING
    def Render(self):
        self.pygame_window.fill(Color.WHITE)
        self.DrawGrid()
        
    def DrawGrid(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                pygame.draw.rect(self.pygame_window, self.grid[i][j].color, self.grid[i][j])
                pygame.draw.rect(self.pygame_window, self.grid[i][j].border_color, self.grid[i][j], 1)
