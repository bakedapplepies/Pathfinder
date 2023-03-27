import pygame
import math
import os

from main import Window
from Node import Node
from constants import *


class Grid(list):
    def __init__(self, window: Window):
        self.window = window
        
        self.sideLength = 20
        
        self.rowStart: int = None
        self.columnStart: int = None
        self.rowDestination: int = None
        self.columnDestination: int = None
        
        # load grid
        if os.path.isfile("save_data/ColorGrid.dat"):
            self.colorGrid = window.saveloadManager.load("ColorGrid")
        else:
            self.colorGrid = list()
        
        # reinitialize main grid from saved color grid
        if len(self.colorGrid) == 0:
            for y in range(0, GRID_RESOLUTION[1], self.sideLength):
                super().append([])
                row = int(y/self.sideLength)
                self.colorGrid.append([])
                
                for x in range(0, GRID_RESOLUTION[0], self.sideLength):
                    super().__getitem__(row).append(Node(x, y, self.sideLength, self.sideLength))
                    self.colorGrid.__getitem__(row).append(Color.WHITE)
                    
        else:
            for y in range(0, GRID_RESOLUTION[1], self.sideLength):
                super().append([])
                row = int(y/self.sideLength)
                
                for x in range(0, GRID_RESOLUTION[0], self.sideLength):
                    col = int(x/self.sideLength)
                    
                    super().__getitem__(row).append(Node(x, y, self.sideLength, self.sideLength))
                    
                    if self.colorGrid[row][col] == Color.BLACK:
                        self.__getitem__(row)[col].setState(NodeState.WALL, self, (row, col))
                        
                    elif self.colorGrid[row][col] == Color.PASTEL_LIME:
                        self.__getitem__(row)[col].setState(NodeState.OBSTACLE, self, (row, col))
                        
                    elif self.colorGrid[row][col] == Color.RED:
                        self.__getitem__(row)[col].setState(NodeState.START, self, (row, col))
                        
                    elif self.colorGrid[row][col] == Color.BLUE:
                        self.__getitem__(row)[col].setState(NodeState.DESTINATION, self, (row, col))
                        
        # redraw grid after each initialization
        for row in range(len(self)):
            for col in range(len(self[0])):
                pygame.draw.rect(window.pygame_window, self[row][col].color, self[row][col], 0, 2)
                pygame.draw.rect(window.pygame_window, self[row][col].border_color, self[row][col], 1, 2)
                    
    def getNeighbors(self, nodePos: tuple) -> tuple:
        row = nodePos[0]
        col = nodePos[1]
        return (
            (
                max(row - 1, 0),
                col
            ),
            (
                min(row + 1, len(self) - 1),
                col
            ),
            (
                row,
                min(col + 1, len(self[0]) - 1)
            ),
            (
                row,
                max(col - 1, 0)
            )
        )
        
    def getManhattanDistance(self, node1: tuple, node2: tuple):
        (row1, col1) = node1
        (row2, col2) = node2
        drow = abs(row1 - row2)
        dcol = abs(col1 - col2)
        return (drow + dcol) * self[row2][col2].cost
    
    def getEuclideanDistance(self, node1: tuple, node2: tuple):
        (row1, col1) = node1
        (row2, col2) = node2
        drow = abs(row1 - row2)
        dcol = abs(col1 - col2)
        return math.sqrt(drow ** 2 + dcol ** 2) * self[row2][col2].cost
                
    def getNode(self, tup: tuple) -> Node:
        return self[tup[0]][tup[1]]    
    
    def setStartNode(self, row: int, col: int) -> None:
        if self.rowStart != None and (row != self.rowStart or col != self.columnStart) and (row < len(self) and col < len(self[0])):
            self[self.rowStart][self.columnStart].setState(NodeState.PATH, self, (self.rowStart, self.columnStart))
        self.rowStart = row
        self.columnStart = col
    
    def setDestinationNode(self, row: int, col: int) -> None:
        if self.rowDestination != None and (row != self.rowDestination or col != self.columnDestination) and (row < len(self) and col < len(self[0])):
            self[self.rowDestination][self.columnDestination].setState(NodeState.PATH, self, (self.rowDestination, self.columnDestination))
        self.rowDestination = row
        self.columnDestination = col
    