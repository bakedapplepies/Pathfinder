import pygame
import heapq
import logging
from queue import PriorityQueue

from Window import Window
from Grid import *
from constants import *


def Dijkstra(grid: Grid, window: Window) -> None:
    start = (grid[grid.rowStart][grid.columnStart].cost, grid.rowStart, grid.columnStart)
    destination = (grid[grid.rowDestination][grid.columnDestination].cost, grid.rowDestination, grid.columnDestination)
    
    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = dict()
    cost_so_far = dict()
    came_from[start] = None
    cost_so_far[start] = 0
        
    while not frontier.empty():
        if not window.paused:
            current = frontier.get()[1]  # only get the node, not the priority
            
            for nextNode in grid.getNeighbors(current):
                new_cost = cost_so_far[current] + grid.getDistance(current, nextNode)
                
                if nextNode == destination:
                    # traceback to start
                    while current != start:
                        grid[current[1]][current[2]].setState(NodeState.OPTIMAL_PATH)
                        current = came_from[current]
                    return None
                
                if grid[nextNode[1]][nextNode[2]].color == Color.BLACK:
                    continue
                
                if nextNode not in cost_so_far or new_cost < cost_so_far[nextNode]:
                    cost_so_far[nextNode] = new_cost
                    print(new_cost)
                    priority = new_cost
                    frontier.put((priority, nextNode))
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
