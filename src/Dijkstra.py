from queue import PriorityQueue

from main import Window
from Grid import Grid
from constants import *


def Dijkstra(grid: Grid, window: Window) -> None:
    start = (grid.rowStart, grid.columnStart)
    destination = (grid.rowDestination, grid.columnDestination)
    
    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = dict()
    cost_so_far = dict()
    came_from[start] = None
    cost_so_far[start] = 0
        
    while not frontier.empty():
        
        window.calculateDeltaTime()
        window.sceneManager.PollInput()
        
        if not window.paused:
            current = frontier.get()[1]
            current_node = grid.getNode(current)
            
            if window.sceneManager.pathfinder.forcePrintFrontier:
                current_node.setState(NodeState.EXPLORED, grid)
                if frontier.empty():
                    break
            
            else:
                for nextNode in grid.getNeighbors(current):
                    
                    if nextNode == destination:
                        # traceback to start
                        while current != start:
                            window.sceneManager.PollInput()
                            window.calculateDeltaTime()
                            
                            current_node = grid.getNode(current)
                            current_node.setState(NodeState.OPTIMAL_PATH, grid)
                            current = came_from[current]
                                                        
                            # keeping the window alive
                            window.sceneManager.Render()
                            
                        return None
                    
                    if current_node.color == Color.BLACK:
                        continue
                    
                    new_cost = cost_so_far[current] + grid.getManhattanDistance(current, nextNode)
                    
                    if nextNode not in cost_so_far or new_cost < cost_so_far[nextNode]:
                        cost_so_far[nextNode] = new_cost
                        priority = new_cost
                        frontier.put((priority, nextNode))
                        came_from[nextNode] = current
                        grid.getNode(nextNode).setState(NodeState.EXPLORED, grid)

        # keeping the window alive
        window.sceneManager.Render()
