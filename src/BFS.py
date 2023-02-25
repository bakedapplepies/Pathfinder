import pygame
import logging
from queue import Queue

from Window import Window
from Grid import *
from constants import *


# TODO: could try implementing saving reached node each time BFS is run

def BreadthFirstSearch(grid: Grid, window: Window) -> None:
    frontier = Queue()
    frontier.put((grid.rowStart, grid.columnStart))
    reached = set()
    reached.add((grid.rowStart, grid.columnStart))
        
    while not frontier.empty():
        if not window.paused:
            current = frontier.get()
            for nextNode in grid.getNeighbors(current):
                if grid[nextNode[0]][nextNode[1]].color == BLUE:
                    return None
                if grid[nextNode[0]][nextNode[1]].color == BLACK:
                    continue
                if nextNode not in reached:
                    frontier.put(nextNode)
                    reached.add(nextNode)
                    grid[nextNode[0]][nextNode[1]].setState(NodeState.Explored)

        # keeping the window alive
        window.sceneManager.PollInput()
        if window.sceneManager.menu.BFS_delay == "On":
            window.sceneManager.Render()
        pygame.display.update()
        # window.clock.tick(FPS)
        window.showFPS()
