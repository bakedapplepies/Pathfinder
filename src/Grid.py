import pygame
import numpy

class Node(pygame.Rect):
    def __init__(self, x, y, dx, dy):
        super().__init__(x, y, dx, dy)


class Grid(numpy.ndarray):
    def __init__(self, resolution: tuple):
        super().__init__()

        self.listGrid = []
        self.sideLength = 20
        
        for i in range(0, resolution[1], self.sideLength):
            self.listGrid.append([])
            for j in range(0, resolution[0], self.sideLength):
                self.listGrid[int(i/self.sideLength)].append(Node(i, j, self.sideLength, self.sideLength))

        self = numpy.array(self.listGrid, dtype=Node)
