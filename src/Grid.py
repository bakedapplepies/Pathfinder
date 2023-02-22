import pygame

from Node import Node
from constants import *


class Grid(list):
    def __init__(self, resolution):
        self.sideLength = 20
        
        self.rowStart: int = None
        self.columnStart: int = None
        self.rowDestination: int = None
        self.columnDestination: int = None
        
        for i in range(0, resolution[1], self.sideLength):
            super().append([])
            for j in range(0, resolution[0], self.sideLength):
                super().__getitem__(int(i/self.sideLength)).append(Node(j, i, self.sideLength, self.sideLength))
                
    def getNeighbors(self, nodePos: tuple):
        row = nodePos[0]
        col = nodePos[1]
        return (
            (max(row - 1, 0), col),
            (row, min(col + 1, len(self[0]) - 1)),
            (min(row + 1, len(self) - 1), col),
            (row, max(col - 1, 0))
        )
                
    def setStartNode(self, x: int, y: int) -> None:
        row = int(y / self.sideLength)
        column = int(x / self.sideLength)
        if self.rowStart != None and (row != self.rowStart or column != self.columnStart) and (row < len(self) and column < len(self[0])):
            self[self.rowStart][self.columnStart].setState(NodeState.Path)
        self.rowStart = row
        self.columnStart = column
    
    def setDestinationNode(self, x: int, y: int) -> None:
        row = int(y / self.sideLength)
        column = int(x / self.sideLength)
        if self.rowDestination != None and (row != self.rowDestination or column != self.columnDestination) and (row < len(self) and column < len(self[0])):
            self[self.rowDestination][self.columnDestination].setState(NodeState.Path)
        self.rowDestination = row
        self.columnDestination = column
            