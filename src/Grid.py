import pygame
import numpy

class Node(pygame.Rect):
    def __init__(self, x, y, dx, dy):
        super().__init__(x, y, dx, dy)


class Grid(numpy.ndarray):
    def __init__(self, resolution):
        super().__init__()
        self.size = 20
        self = numpy.zeros(shape=2, dtype=Node)
        
        
