import pygame
from queue import PriorityQueue

from main import Window
from Grid import *
from constants import *


def GreedyBFS(grid: Grid, window: Window) -> None:
    start = (grid.rowStart, grid.columnStart)
    destination = (grid.rowDestination, grid.columnDestination)
    
    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = dict()
    came_from[start] = None
        
    while not frontier.empty():
        if not window.paused:
            if window.sceneManager.pathfinder.forcePrintFrontier:
                current = frontier.get()
                grid[current[1][0]][current[1][1]].setState(NodeState.EXPLORED)
                if frontier.empty():
                    break
                
            else:
                current = frontier.get()[1]  # only get the node, not the priority
                
                for nextNode in grid.getNeighbors(current):                
                    # traceback to start
                    if nextNode == destination:
                        while current != start:
                            grid[current[0]][current[1]].setState(NodeState.OPTIMAL_PATH)
                            current = came_from[current]
                            
                            # keeping the window alive
                            window.calculateDeltaTime()
                            
                            window.sceneManager.PollInput()
                            if window.sceneManager.menu.delay == "On" and window.sceneManager.scene == Scenes.PATHFINDER:
                                window.sceneManager.Render()
                            elif window.sceneManager.scene == Scenes.MENU:
                                window.sceneManager.Render()
                            pygame.display.update()
                            
                        return None
                    
                    if grid[nextNode[0]][nextNode[1]].color == Color.BLACK:
                        continue
                    
                    if nextNode not in came_from:
                        priority = grid.getDistance(destination, nextNode)
                        frontier.put((priority, nextNode))
                        came_from[nextNode] = current
                        grid[nextNode[0]][nextNode[1]].setState(NodeState.EXPLORED)

        # keeping the window alive
        window.calculateDeltaTime()
        
        window.sceneManager.PollInput()
        if window.sceneManager.menu.delay == "On" and window.sceneManager.scene == Scenes.PATHFINDER:
            window.sceneManager.Render()
        elif window.sceneManager.scene == Scenes.MENU:
            window.sceneManager.Render()
        pygame.display.update()
