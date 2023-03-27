from queue import PriorityQueue

from main import Window
from Grid import Grid
from constants import *


def AStar(grid: Grid, window: Window) -> None:
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
            (priority, currentPos) = frontier.get()
            current_node = grid.getNode(currentPos)
            
            if window.sceneManager.pathfinder.forcePrintFrontier:
                current_node.setState(NodeState.EXPLORED, grid)
                if frontier.empty():
                    break
            
            else:
                for nextNodePos in grid.getNeighbors(currentPos):
                    
                    if nextNodePos == destination:
                        # traceback to start
                        while currentPos != start:
                            window.sceneManager.PollInput()
                            window.calculateDeltaTime()
                            
                            current_node = grid.getNode(currentPos)
                            current_node.setState(NodeState.OPTIMAL_PATH, grid)
                            currentPos = came_from[currentPos]
                                                        
                            # keeping the window alive
                            window.sceneManager.Render()
                            
                        return None
                    
                    if grid.getNode(nextNodePos).color == Color.BLACK:
                        continue
                    
                    cost_from_start = cost_so_far[currentPos] + 1 * grid.getNode(nextNodePos).cost
                    
                    if nextNodePos not in cost_so_far or cost_from_start < cost_so_far[nextNodePos]:
                        cost_so_far[nextNodePos] = cost_from_start
                        priority = cost_from_start + grid.getManhattanDistance(nextNodePos, destination)
                        # print(grid.getManhattanDistance(nextNodePos, destination))
                        frontier.put((priority, nextNodePos))
                        came_from[nextNodePos] = currentPos
                        grid.getNode(nextNodePos).setState(NodeState.EXPLORED, grid)

        # keeping the window alive
        window.sceneManager.Render()
