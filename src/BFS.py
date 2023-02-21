from queue import Queue

from Grid import *


def BreadthFirstSearch(grid: Grid):
    frontier = Queue()
    frontier.put(grid[grid.rowStart][grid.columnStart])
    reached = set()
    reached.add(grid[grid.rowStart][grid.columnStart])
    
    while not frontier.empty():
        current = frontier.get()
        for next in grid.getNeighbors(current):
            if next not in reached:
                next.setState("Explored")
                frontier.put(next)
                reached.add(next)
