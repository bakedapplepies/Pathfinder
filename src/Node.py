import pygame

from constants import *


class Node(pygame.Rect):
    def __init__(self, x, y, dx, dy):
        super().__init__(x, y, dx, dy)
        self.color = WHITE
        self.border_color = BLACK

    def setState(self, state: str, grid = None, pos: tuple = None):
        if state == NodeState.Path:
            self.color = WHITE
        elif state == NodeState.Wall and not (self.color == RED or self.color == BLUE):
            self.color = BLACK
        elif state == NodeState.Start:
            self.color = RED
            grid.setStartNode(pos[0], pos[1])
        elif state == NodeState.Destination:
            self.color = BLUE
            grid.setDestinationNode(pos[0], pos[1])
        elif state == NodeState.Explored:
            self.color = GREY