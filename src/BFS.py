import pygame
import logging
from queue import Queue

from Window import Window
from Grid import *
from constants import *


def BreadthFirstSearch(grid: Grid, window: Window) -> None:
    frontier = Queue()
    frontier.put((grid.rowStart, grid.columnStart))
    reached = set()
    reached.add((grid.rowStart, grid.columnStart))
    
    cumulative_time = 0.5
    
    while not frontier.empty():
        current = frontier.get()
        for nextNode in grid.getNeighbors(current):
            if grid[nextNode[0]][nextNode[1]].color == BLUE:
                return None
            elif grid[nextNode[0]][nextNode[1]].color == BLACK:
                continue
            if nextNode not in reached:
                frontier.put(nextNode)
                reached.add(nextNode)
                grid[nextNode[0]][nextNode[1]].setState(NodeState.Explored)
