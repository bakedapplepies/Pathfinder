import pygame

from constants import *


class Node(pygame.Rect):
    def __init__(self, x, y, dx, dy):
        super().__init__(x, y, dx, dy)
        self.color = Color.WHITE
        self.border_color = Color.BLACK
        
        self.cost = 1

    def setState(self, state: str, grid=None, pos: tuple=None):
        if state == NodeState.PATH:
            self.color = Color.WHITE
            self.cost = 1
            
        elif state == NodeState.WALL and not (self.color == Color.RED or self.color == Color.BLUE):
            self.color = Color.BLACK
            
        elif state == NodeState.START:
            self.color = Color.RED
            self.cost = 0
            grid.setStartNode(pos[0], pos[1])
            
        elif state == NodeState.DESTINATION:
            self.color = Color.BLUE
            self.cost = 0
            grid.setDestinationNode(pos[0], pos[1])
            
        elif state == NodeState.EXPLORED:
            self.color = Color.GREY
            
        elif state == NodeState.OPTIMAL_PATH:
            self.color = Color.PURPLE
            