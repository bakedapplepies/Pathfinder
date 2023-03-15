import os

from main import Window
from Node import Node
from constants import *


class Grid(list):
    def __init__(self, window: Window):
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
            for i in range(0, RESOLUTION[1], self.sideLength):
                super().append([])
                row = int(i/self.sideLength)
                self.colorGrid.append([])
                
                for j in range(0, RESOLUTION[0], self.sideLength):
                    super().__getitem__(row).append(Node(j, i, self.sideLength, self.sideLength))
                    self.colorGrid.__getitem__(row).append(Color.WHITE)
                    
        else:
            for i in range(0, RESOLUTION[1], self.sideLength):
                super().append([])
                row = int(i/self.sideLength)
                
                for j in range(0, RESOLUTION[0], self.sideLength):
                    col = int(j/self.sideLength)
                    
                    super().__getitem__(row).append(Node(j, i, self.sideLength, self.sideLength))
                    
                    if self.colorGrid[row][col] == Color.BLACK:
                        self[row][col].setState(NodeState.WALL, self, (row, col))
                        
                    elif self.colorGrid[row][col] == Color.PASTEL_LIME:
                        self[row][col].setState(NodeState.OBSTACLE, self, (row, col))
                        
                    elif self.colorGrid[row][col] == Color.RED:
                        self.setStartNode(row, col)
                        self[row][col].setState(NodeState.START, self, (row, col))
                        
                    elif self.colorGrid[row][col] == Color.BLUE:
                        self.setDestinationNode(row, col)
                        self[row][col].setState(NodeState.DESTINATION, self, (row, col))
            
            
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
        
    def getDistance(self, node1: tuple, node2: tuple):
        # return (abs(node1[0] - node2[0]) + abs(node1[1] - node2[1])) * max(self[node1[0]][node1[1]].cost, self[node2[0]][node2[1]].cost)
        return (pow(node1[0] - node2[0], 2) + pow(node1[1] - node2[1], 2)) + (abs(node1[0] - node2[0]) + abs(node1[1] - node2[1]))#* max(self[node1[0]][node1[1]].cost, self[node2[0]][node2[1]].cost)
                
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
    