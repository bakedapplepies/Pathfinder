import pygame

from constants import *


class Node(pygame.Rect):
    def __init__(self, x, y, dx, dy):
        super().__init__(x, y, dx, dy)
        self.color = WHITE
        self.border_color = BLACK
        self.border = 1

    def setState(self, state: str):
        if state == "Path":
            self.color = WHITE
        elif state == "Wall":
            self.color = BLACK
        elif state == "Start":
            self.color = RED
        elif state == "Destination":
            self.color = BLUE


class Grid(list):
    def __init__(self, resolution):
        self.sideLength = 20

        print(f"res: {resolution[0]}x{resolution[1]}")
        
        for i in range(0, resolution[1], self.sideLength):
            super().append([])
            for j in range(0, resolution[0], self.sideLength):
                super().__getitem__(int(i/self.sideLength)).append(Node(j, i, self.sideLength, self.sideLength))
