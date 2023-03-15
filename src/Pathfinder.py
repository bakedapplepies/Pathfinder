import pygame
import sys

from main import Window
from AbstractScene import AbstractScene
from Grid import Grid
from Node import Node
from BFS import BreadthFirstSearch
from Dijkstra import Dijkstra
from GreedyBFS import GreedyBFS
from AStar import AStar
from constants import *


class Pathfinder(AbstractScene):
    def __init__(self, window: Window):
        # window
        self.window = window
        self.pygame_window = window.pygame_window
        
        # Grid
        self.grid = Grid(window=self.window)
        
        # Variables
        self.forcePrintFrontier = False

    # INPUTS
    def PollInput(self):
        keydown = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.window.saveloadManager.save("ColorGrid", self.grid.colorGrid)
                self.window.sceneManager.menu.saveSettings()
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.VIDEORESIZE:
                # self.window = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                self.grid = Grid(self.window)
                
            if event.type == pygame.KEYDOWN:
                keydown = True
                
            mouse_clicks = pygame.mouse.get_pressed()
            if mouse_clicks:
                mouse_pos = pygame.mouse.get_pos()
                
                row = min(int(mouse_pos[1]/self.grid.sideLength), len(self.grid)-1)
                col = min(int(mouse_pos[0]/self.grid.sideLength), len(self.grid[0])-1)
                grid_pos = (row, col)
                
                node: Node = self.grid[row][col]
                
                if self.window.sceneManager.menu.mouse_mode == "Mouse":
                    if pygame.mouse.get_pressed()[2]:
                        node.setState(NodeState.PATH, self.grid, grid_pos)
                    
                    elif pygame.mouse.get_pressed()[0]:
                        if not pygame.key.get_pressed()[pygame.K_LCTRL]:
                            node.setState(NodeState.WALL, self.grid, grid_pos)
                        else:
                            node.setState(NodeState.OBSTACLE, self.grid, grid_pos)
                    
                    elif pygame.mouse.get_pressed()[1]:
                        if not pygame.key.get_pressed()[pygame.K_LCTRL]:
                            node.setState(NodeState.START, self.grid, grid_pos)
                        else:
                            node.setState(NodeState.DESTINATION, self.grid, grid_pos)
                
                elif self.window.sceneManager.menu.mouse_mode == "Trackpad":
                    if pygame.mouse.get_pressed()[2]:
                        node.setState(NodeState.PATH, self.grid, grid_pos)
                    
                    elif pygame.mouse.get_pressed()[0]:
                        pressed_keys = pygame.key.get_pressed()
                        
                        if pressed_keys[pygame.K_1]:
                            node.setState(NodeState.OBSTACLE, self.grid, grid_pos)
                        elif pressed_keys[pygame.K_w]:
                            node.setState(NodeState.WALL, self.grid, grid_pos)
                        elif not pygame.key.get_pressed()[pygame.K_LCTRL]:
                            node.setState(NodeState.START, self.grid, grid_pos)
                        else:
                            node.setState(NodeState.DESTINATION, self.grid, grid_pos)
        
        keys = pygame.key.get_pressed()
        
        # run Pathfinder Algorithm
        if keys[pygame.K_b] and keydown and self.grid.rowStart != None and self.grid.rowDestination != None:
            # reload saved grid
            self.resetExploredNodes()
            
            self.forcePrintFrontier = False
            
            if self.window.sceneManager.menu.algorithm == Algorithms.BFS:
                BreadthFirstSearch(self.grid, self.window)
            elif self.window.sceneManager.menu.algorithm == Algorithms.DIJKSTRA:
                Dijkstra(self.grid, self.window)
            elif self.window.sceneManager.menu.algorithm == Algorithms.GREEDY_BFS:
                GreedyBFS(self.grid, self.window)
            elif self.window.sceneManager.menu.algorithm == Algorithms.ASTAR:
                AStar(self.grid, self.window)
                
                
        # Menu
        elif keys[pygame.K_ESCAPE] and keydown:
            self.window.paused = True
            self.window.sceneManager.switchScene(Scenes.MENU)
            
        # New Grid
        elif keys[pygame.K_g] and keydown:
            newColorGrid = list()
            for i in range(len(self.grid)):
                newColorGrid.append([])
                for j in range(len(self.grid[0])):
                    newColorGrid[i].append(Color.WHITE)
                    
            self.window.saveloadManager.save("ColorGrid", newColorGrid)
            self.grid = Grid(window=self.window)
            
        # Force Get all Frontier nodes
        elif keys[pygame.K_f] and keydown:
            self.forcePrintFrontier = not self.forcePrintFrontier

    # RENDERING
    def Render(self):
        self.pygame_window.fill(Color.WHITE)
        self.DrawGrid()
        
    def DrawGrid(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                pygame.draw.rect(self.pygame_window, self.grid[i][j].color, self.grid[i][j], 0, 2)
                pygame.draw.rect(self.pygame_window, self.grid[i][j].border_color, self.grid[i][j], 1, 2)
                
    def resetExploredNodes(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                self.grid[i][j].color = self.grid.colorGrid[i][j]
