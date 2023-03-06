import pygame
import logging
from queue import Queue

from Window import Window
from Grid import *
from constants import *


def BreadthFirstSearch(grid: Grid, window: Window) -> None:
    start = (grid[grid.rowStart][grid.columnStart].cost, grid.rowStart, grid.columnStart)
    destination = (grid[grid.rowDestination][grid.columnDestination].cost, grid.rowDestination, grid.columnDestination)
    
    frontier = Queue()
    frontier.put(start)
    came_from = dict()
    came_from[start] = None
        
    while not frontier.empty():
        if not window.paused:
            current = frontier.get()
            for nextNode in grid.getNeighbors(current):
                if nextNode == destination:
                    # traceback to start
                    while current != start:
                        grid[current[1]][current[2]].setState(NodeState.OPTIMAL_PATH)
                        current = came_from[current]
                        
                    return None
                
                if grid[nextNode[1]][nextNode[2]].color == Color.BLACK:
                    continue
                
                if nextNode not in came_from:
                    frontier.put(nextNode)
                    came_from[nextNode] = current
                    grid[nextNode[1]][nextNode[2]].setState(NodeState.EXPLORED)

        # keeping the window alive
        window.calculateDeltaTime()
        
        window.sceneManager.PollInput()
        if window.sceneManager.menu.delay == "On" and window.sceneManager.scene == Scenes.PATHFINDER:
            window.sceneManager.Render()
        elif window.sceneManager.scene == Scenes.MENU:
            window.sceneManager.menu.Render()
        pygame.display.update()
