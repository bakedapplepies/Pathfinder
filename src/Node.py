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
            grid.colorGrid[pos[0]][pos[1]] = Color.WHITE
            self.cost = 1
            
        elif state == NodeState.WALL and not (self.color == Color.RED or self.color == Color.BLUE):
            self.color = Color.BLACK
            grid.colorGrid[pos[0]][pos[1]] = Color.BLACK
            
        elif state == NodeState.OBSTACLE:
            self.color = Color.PASTEL_LIME
            grid.colorGrid[pos[0]][pos[1]] = Color.PASTEL_LIME
            self.cost = 5
            
        elif state == NodeState.START:
            self.color = Color.RED
            grid.colorGrid[pos[0]][pos[1]] = Color.RED
            grid.setStartNode(row=pos[0], col=pos[1])
            self.cost = 1
            
        elif state == NodeState.DESTINATION:
            self.color = Color.BLUE
            grid.colorGrid[pos[0]][pos[1]] = Color.BLUE
            grid.setDestinationNode(row=pos[0], col=pos[1])
            self.cost = 1
            
        elif state == NodeState.EXPLORED:
            self.color = tuple(i*0.82 for i in self.color)
            
        elif state == NodeState.OPTIMAL_PATH:
            self.color = Color.PURPLE
            