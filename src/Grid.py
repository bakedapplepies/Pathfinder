import pygame
import numpy

from constants import *


class Node(pygame.Rect):
    def __init__(self, x, y, dx, dy):
        super().__init__(x, y, dx, dy)
        self.color = BLACK
        self.border = 0

    def setState(self, state: str):
        if state == "Path":
            self.color = BLACK
            self.border = 1
        elif state == "Wall":
            self.color = BLACK
            self.border = 0


class Grid(numpy.ndarray):
    def __init__(self):
        super().__init__()

    def __new__(self, resolution):
        self.listGrid = []
        self.sideLength = 20

        print(f"res: {resolution[0]}x{resolution[1]}")
        
        for i in range(0, resolution[1], self.sideLength):
            self.listGrid.append([])
            for j in range(0, resolution[0], self.sideLength):
                self.listGrid[int(i/self.sideLength)].append(Node(j, i, self.sideLength, self.sideLength))

        return numpy.array(self.listGrid, dtype=Node)
