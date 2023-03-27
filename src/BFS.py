from queue import Queue

from main import Window
from Grid import Grid
from constants import *


def BreadthFirstSearch(grid: Grid, window: Window) -> None:
    start = (grid.rowStart, grid.columnStart)
    destination = (grid.rowDestination, grid.columnDestination)
    
    frontier = Queue()
    frontier.put(start)
    came_from = dict()
    came_from[start] = None
        
    while not frontier.empty():
        
        window.calculateDeltaTime()
        window.sceneManager.PollInput()
        
        if not window.paused:
            currentPos = frontier.get()
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
                    
                    if nextNodePos not in came_from:
                        frontier.put(nextNodePos)
                        came_from[nextNodePos] = currentPos
                        grid.getNode(nextNodePos).setState(NodeState.EXPLORED, grid)

        # keeping the window alive
        window.sceneManager.Render()
