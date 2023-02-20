import pygame

from constants import *


class Grid(list):
    def __init__(self, resolution):
        self.sideLength = 20
        
        self.rowStart: int = None
        self.columnStart: int = None
        self.rowDestination: int = None
        self.columnDestination: int = None

        print(f"res: {resolution[0]}x{resolution[1]}")
        
        for i in range(0, resolution[1], self.sideLength):
            super().append([])
            for j in range(0, resolution[0], self.sideLength):
                super().__getitem__(int(i/self.sideLength)).append(Node(j, i, self.sideLength, self.sideLength))
                
    def setStartNode(self, x: int, y: int):
        row = int(y / self.sideLength)
        column = int(x / self.sideLength)
        if self.rowStart != None and (row != self.rowStart or column != self.columnStart) and (row < len(self) and column < len(self[0])):
            self[self.rowStart][self.columnStart].setState("Path")
        self.rowStart = row
        self.columnStart = column
    
    def setDestinationNode(self, x: int, y: int):
        row = int(y / self.sideLength)
        column = int(x / self.sideLength)
        if self.rowDestination != None and (row != self.rowDestination or column != self.columnDestination) and (row < len(self) and column < len(self[0])):
            self[self.rowDestination][self.columnDestination].setState("Path")
        self.rowDestination = row
        self.columnDestination = column
        
    
class Node(pygame.Rect):
    def __init__(self, x, y, dx, dy):
        super().__init__(x, y, dx, dy)
        self.color = WHITE
        self.border_color = BLACK

    def setState(self, state: str, grid: Grid = None, pos: tuple = None):
        if state == "Path":
            self.color = WHITE
        elif state == "Wall" and not (self.color == RED or self.color == BLUE):
            self.color = BLACK
        elif state == "Start":
            self.color = RED
            grid.setStartNode(pos[0], pos[1])
        elif state == "Destination":
            self.color = BLUE
            grid.setDestinationNode(pos[0], pos[1])
            